import { reservationFormController } from "../controllers/reservationForm.controller";
import { createReservation } from "../services/reservation.service";

export default function reservationForm() {
    setTimeout(() => {
        document
            .getElementById("btnCancelRservationForm")
            ?.addEventListener("click", () => {
                reservationFormController();
            })
        document
            .getElementById('formCreateReservation')
            .addEventListener('submit', (e) => {
                e.preventDefault()
                const user = localStorage.getItem('user')
                const form = {
                    workspace: document.getElementById('sala').value.toLowerCase(),
                    date: document.getElementById('fecha').value,
                    startHour: document.getElementById('hora-inicio').value,
                    endHour: document.getElementById('hora-fin').value,
                    reason: document.getElementById('motivo').value
                }

                for (const [key, value] of Object.entries(form)) {
                    if (!value) {
                        alert('Todos los campos deben ser llenados')
                        return
                    }
                }

                const form_ = {
                    workspace: document.getElementById('sala').value.toLowerCase(),
                    date: document.getElementById('fecha').value,
                    startHour: document.getElementById('hora-inicio').value,
                    endHour: document.getElementById('hora-fin').value,
                    reason: document.getElementById('motivo').value,
                    status: "pending",
                    userId: Number(user.id),
                } 

                createReservation(form_)
                window.history.pushState({}, '', '/home')
                router()
                return
            })
    });


    return `
    <div class="min-h-screen bg-gray-50 p-6 sm:p-12">
        <div class="max-w-xl mx-auto bg-white rounded-lg shadow-sm border border-gray-200">

        <!-- Encabezado del Formulario -->
        <div class="px-6 py-4 border-b border-gray-200">
            <h2 class="text-xl font-bold text-gray-800">Crear Nueva Reserva</h2>
            <p class="text-sm text-gray-500 mt-1">Completa los datos para asignar una sala.</p>
        </div>

        <!-- Cuerpo del Formulario -->
        <form id='formCreateReservation' class="p-6 space-y-5">

            <!-- Selección de Sala -->
            <div>
            <label for="sala" class="block text-sm font-semibold text-gray-700 mb-1">Sala</label>
            <select id="sala" name="sala"
                class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm text-gray-800">
                <option value="">Selecciona una sala...</option>
                <option value="Private-offices.">Oficinas privadas.</option>
                <option value="Meeting-rooms.">Salas de reuniones.</option>
                <option value="Coworking-spaces.">Espacios de coworking.</option>
                <option value="Auditoriums">Auditorios.</option>
            </select>
            </div>

            <!-- Fecha -->
            <div>
            <label for="fecha" class="block text-sm font-semibold text-gray-700 mb-1">Fecha</label>
            <input type="date" id="fecha" name="fecha" value="2026-01-15"
                class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm text-gray-800" />
            </div>

            <!-- Horarios (Inicio y Fin) -->
            <div class="grid grid-cols-2 gap-4">
            <div>
                <label for="hora-inicio" class="block text-sm font-semibold text-gray-700 mb-1">Hora Inicio</label>
                <input type="time" id="hora-inicio" name="hora-inicio"
                class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm text-gray-800" />
            </div>
            <div>
                <label for="hora-fin" class="block text-sm font-semibold text-gray-700 mb-1">Hora Fin</label>
                <input type="time" id="hora-fin" name="hora-fin"
                class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm text-gray-800" />
            </div>
            </div>

            <!-- Motivo de la reunión -->
            <div>
            <label for="motivo" class="block text-sm font-semibold text-gray-700 mb-1">Motivo</label>
            <input type="text" id="motivo" name="motivo" placeholder="Ej. Sprint Planning o Daily Meeting"
                class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm text-gray-800" />
            </div>

            <!-- Botones de Acción -->
            <div class="flex items-center justify-end space-x-3 pt-4 border-t border-gray-100">
            <button id="btnCancelRservationForm"
                class="px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-800 transition-colors cursor-pointer">
                Cancelar
            </button>
            <button
                class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded shadow-sm transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 cursor-pointer">
                Guardar Reserva
            </button>
            </div>

        </form>
        </div>
    </div>
    `
}