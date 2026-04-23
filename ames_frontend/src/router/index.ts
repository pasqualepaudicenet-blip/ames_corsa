import { createRouter, createWebHistory } from 'vue-router'

import { verifyToken } from "@/utils/auth";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { left: 0, top: 0 }
  },
  routes: [
      {
        path: '/',
        name: 'main',
        component: () => import('@/layouts/MainLayout.vue'),
        children: [
                      {
                        path: '',
                        name: 'Ecommerce',
                        component: () => import('@/views/Ecommerce.vue'),
                        meta: {
                          title: 'eCommerce Dashboard',
                          requiresAuth: true
                        },
                      },
                      {
                        path: 'corse-list',
                        name: 'CorseList',
                        component: () => import('@/views/Corsa/CorseList.vue'),
                        meta: {
                          title: 'Lista corse',
                        },
                      },
                      
                      {
                        path: '/corsa-detail/:id',
                        name: 'CorsaDetail',
                        component: () => import('../views/Corsa/Detail.vue'),
                        meta: {
                          title: 'Calendar',
                        },
                      },
                      {
                        path: 'users-list',
                        name: 'UsersList',
                        component: () => import('@/views/User/UsersList.vue'),
                        meta: {
                          title: 'Lista utenti',
                        },
                      },
                      {
                        path: 'users-detail/:id',
                        name: 'UserDetail',
                        component: () => import('@/views/User/UserDetail.vue'),
                        meta: {
                          title: 'Lista utenti',
                        },
                      },
                      {
                        path: '/profile',
                        name: 'Profile',
                        component: () => import('../views/Others/UserProfile.vue'),
                        meta: {
                          title: 'Profile',
                        },
                      },
                      {
                        path: '/form-elements',
                        name: 'Form Elements',
                        component: () => import('../views/Forms/FormElements.vue'),
                        meta: {
                          title: 'Form Elements',
                        },
                      },
                      {
                        path: '/basic-tables',
                        name: 'Basic Tables',
                        component: () => import('../views/Tables/BasicTables.vue'),
                        meta: {
                          title: 'Basic Tables',
                        },
                      },
                      {
                        path: '/line-chart',
                        name: 'Line Chart',
                        component: () => import('../views/Chart/LineChart/LineChart.vue'),
                      },
                      {
                        path: '/bar-chart',
                        name: 'Bar Chart',
                        component: () => import('../views/Chart/BarChart/BarChart.vue'),
                      },
                      {
                        path: '/alerts',
                        name: 'Alerts',
                        component: () => import('../views/UiElements/Alerts.vue'),
                        meta: {
                          title: 'Alerts',
                        },
                      },
                      {
                        path: '/avatars',
                        name: 'Avatars',
                        component: () => import('../views/UiElements/Avatars.vue'),
                        meta: {
                          title: 'Avatars',
                        },
                      },
                      {
                        path: '/badge',
                        name: 'Badge',
                        component: () => import('../views/UiElements/Badges.vue'),
                        meta: {
                          title: 'Badge',
                        },
                      },

                      {
                        path: '/buttons',
                        name: 'Buttons',
                        component: () => import('../views/UiElements/Buttons.vue'),
                        meta: {
                          title: 'Buttons',
                        },
                      },

                      {
                        path: '/images',
                        name: 'Images',
                        component: () => import('../views/UiElements/Images.vue'),
                        meta: {
                          title: 'Images',
                        },
                      },
                      {
                        path: '/videos',
                        name: 'Videos',
                        component: () => import('../views/UiElements/Videos.vue'),
                        meta: {
                          title: 'Videos',
                        },
                      },
                      {
                        path: '/blank',
                        name: 'Blank',
                        component: () => import('../views/Pages/BlankPage.vue'),
                        meta: {
                          title: 'Blank',
                        },
                      },

                      {
                        path: '/error-404',
                        name: '404 Error',
                        component: () => import('../views/Errors/FourZeroFour.vue'),
                        meta: {
                          title: '404 Error',
                        },
                      },

                      {
                        path: '/signin',
                        name: 'Signin',
                        component: () => import('../views/Auth/Signin.vue'),
                        meta: {
                          title: 'Signin',
                          meta: { public: true }
                        },
                      },
                      {
                        path: '/signup',
                        name: 'Signup',
                        component: () => import('../views/Auth/Signup.vue'),
                        meta: {
                          title: 'Signup',
                        },
                      },
              ],
      },
      
    ]
})
router.beforeEach(async (to, from, next) => {
  const token = localStorage.getItem("access");
  if (to.meta.public) return next();
  if (to.meta.requiresAuth) {
    if (!token) {
      return next("/signin");
    }

    const valid = await verifyToken(token);

    if (!valid) {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      return next("/signin");
    }

    // Refresh token solo se l'access è ancora valido
    try {
      const refreshToken = localStorage.getItem("refresh");
      if (refreshToken) {
        const response = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ refresh: refreshToken }),
        });
        if (response.ok) {
          const data = await response.json();
          localStorage.setItem("access", data.access);
        } else {
          console.error("Errore refresh token");
        }
      }
    } catch (error) {
      console.error("Errore refresh token:", error);
    }
  }

  next();
});



export default router


