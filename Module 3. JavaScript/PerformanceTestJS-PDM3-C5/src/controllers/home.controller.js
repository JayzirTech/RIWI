import ReservationCard from "@components/ReservationCard";
import { getReservation } from "@services/reservation.service"
// import { getSession } from "@/utils"; esto no existe
import { router } from "../router/router";
import { getSessionUser } from "../utils/consultSession";

export const homeController = async () => {
  const container = document.querySelector("#reservationsContainer");

  const user = getSessionUser();

  const reservations = await getReservation();  // Daba error porque estaba mal escrito

  const filteredReservations =
    user.role === "admin"
      ? reservations
      : reservations.filter((reservation) => (reservation.userId) === Number(user.id)); // Acá estaba tomando el id del usuario como string. Por conflictos de tipos de datos, nunca iba a filtrar lo que se quería

  container.innerHTML = container.innerHTML = filteredReservations?.length
    ? filteredReservations
      .map((reservation) => ReservationCard(reservation))
      .join("")
    : `
      <div class="w-full text-center py-8 col-span-2">
        <p class="text-slate-500">
          No hay reservas disponibles
        </p>
      </div>
    `;

  const goToForm = document.getElementById('btnCreateReservation')
  goToForm.addEventListener('click', (e) => {
    e.preventDefault()

    const path = goToForm.closest('a').getAttribute('href');

    window.history.pushState({}, '', path)
    router()
    return
  })

};
