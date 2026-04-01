# 配置为 backend 模式，并且前端的角色 authority 配置任然生效

### 解决方案：修改后端返回的菜单数据

在后端权限模式下，系统是通过后端返回的菜单数据来生成路由的。您可以在后端返回的菜单数据中添加authority属性，这样即使在后端权限模式下，前端的权限检查也能生效。

以下是具体实施步骤：

1. 设置权限模式为后端模式

   ~~~typescript
   // 在 preferences.ts 中配置
   export const overridesPreferences = defineOverridesPreferences({
    app: {
     accessMode: 'backend',
    },
   });
   ~~~

2.确保后端返回的菜单数据中包含authority属性：

如果您使用的是模拟后端数据（如代码中的`MOCK_MENU_LIST`），您可以修改这些数据，为每个菜单项添加authority属性：

~~~typescript
// 示例：在后端返回的菜单数据中添加authority属性

{

 id: xxx,

 path: '/system/menu',

 name: 'SystemMenu',

 component: '/system/menu/list',

 meta: {

  icon: 'mdi:menu',

  title: 'system.menu.title',

  authority: ['admin'], // 添加这个属性

 },

}
~~~



3.修改后端菜单生成逻辑：

如果您有权限修改后端代码或模拟数据，可以在创建菜单数据的函数中添加authority属性：

~~~typescript
// 例如在 mock-data.ts 中的 createDemosMenus 函数中

const createDemosMenus = (role: 'admin' | 'super' | 'user') => {

 return [

  {

   // ...其他属性

   meta: {

​    // ...其他meta属性

​    authority: [role], // 添加这个属性，使用当前角色

   },

   // ...其他菜单属性

  }

 ];

};
~~~



4.修改前端解析逻辑：

您可能需要检查和确保generateRoutesByBackend函数能正确处理菜单数据中的authority属性。从代码中看，这个函数会将后端返回的菜单数据转换为路由配置，但可能不会特别处理authority属性。

5.检查路由守卫：

确保在router.beforeEach中的权限检查逻辑中同时考虑了前端路由配置的authority和后端返回的authority。

### 关键代码解析：

在后端模式下，权限检查的关键是directive.ts中的isAccessible函数：

~~~typescript
function isAccessible(el: Element, binding: DirectiveBinding<string | string[]>) {

 const { accessMode, hasAccessByCodes, hasAccessByRoles } = useAccess();

 const value = binding.value;

 if (!value) return;

 const authMethod =

  accessMode.value === 'frontend' && binding.arg === 'role'

   ? hasAccessByRoles

   : hasAccessByCodes;

 const values = Array.isArray(value) ? value : [value];

 if (!authMethod(values)) {

  el?.remove();

 }

}
~~~

注意这里的逻辑：

- 当accessMode为frontend且binding.arg为role时，使用hasAccessByRoles进行检查

- 否则使用hasAccessByCodes进行检查

这意味着在后端模式下，默认使用权限码（hasAccessByCodes）而非角色（hasAccessByRoles）进行检查。

### 推荐的解决方案：

1.修改后端返回的菜单数据：

- 在后端API返回的菜单数据中添加authority属性

- 确保这个authority属性的值与您的角色匹配

2.创建自定义中间件：

- 创建一个自定义的路由middleware，在原有权限检查逻辑基础上添加对authority的检查

- 这样可以在后端模式下也执行前端模式的权限检查逻辑

3.修改accessible.ts中的生成路由逻辑：

- 修改generateRoutes函数，使其在后端模式下也执行hasAuthority检查

### 示例实现：

以下是一种可行的实现方式，通过修改accessible.ts中的generateRoutes函数：

~~~typescript
async function generateRoutes(

 mode: AccessModeType,

 options: GenerateMenuAndRoutesOptions,

) {

 const { forbiddenComponent, roles, routes } = options;

 let resultRoutes: RouteRecordRaw[] = routes;

 switch (mode) {

  case 'backend': {

   // 获取后端路由

   resultRoutes = await generateRoutesByBackend(options);

   // 添加：使用前端权限检查逻辑过滤后端路由

   if (roles && roles.length > 0) {

​    resultRoutes = filterTree(resultRoutes, (route) => {

​     return hasAuthority(route, roles);

​    });

   }

   break;

  }

  case 'frontend': {

   resultRoutes = await generateRoutesByFrontend(

​    routes,

​    roles || [],

​    forbiddenComponent,

   );

   break;

  }

 }

 // 其余处理...

}
~~~

这样修改后，即使在后端权限模式下，也会使用hasAuthority函数检查路由的authority属性，从而实现您想要的功能。

注意：这种修改可能会影响系统的整体权限逻辑，请确保在开发环境中充分测试后再应用到生产环境。