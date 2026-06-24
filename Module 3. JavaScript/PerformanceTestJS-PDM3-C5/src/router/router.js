import loginView from "@/views/loginView";
import homeView from "@/views/homeView";
import { getSessionUser, getUserRole } from "../utils/consultSession";
import NotFoundView from "../views/notFound";
import reservationForm from "../views/reservationForm";

const routes = {
  "/": {
    view: loginView,
    allowedRoles: []
  },

  "/home": {
    view: homeView,
    allowedRoles: ['admin', 'user']
  },
  "/notFound": {
    view: NotFoundView,
    allowedRoles: []
  },

  "/createReservation":{
    view: reservationForm,
    allowedRoles: ['admin', 'user']
  }
};

export const navigateTo = (path) => {
  history.pushState({}, "", path);
  router();
};

export const router = () => {
  const app = document.querySelector("#app");

  const path = window.location.pathname;

  const routeMatch = routes[path] || routes['/notFound'];

  const { view, allowedRoles } = routeMatch

  const userRole = getUserRole()

  if (allowedRoles && allowedRoles.length > 0) {

    if (!userRole) {
      console.log('No estás autenticado')
      window.history.pushState({}, '', '/')
      router()
      return
    }
  }

  if (userRole && path === '/') {
    console.log('Estás autenticado')
    window.history.pushState({}, '', '/home')
    router()
    return
  }

  app.innerHTML = view();
};

window.addEventListener("popstate", router);
