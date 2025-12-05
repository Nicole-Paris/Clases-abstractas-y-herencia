import { Chart, registerables } from "chart.js"; // 👈 importa todo lo necesario

Chart.register(...registerables); // 👈 registra todos los componentes
export class ChartEngine {
  async initialize() {
    console.time("ChartEngine");
    console.log("⏳ Inicializando ChartEngine...");

    await new Promise((r) => setTimeout(r, 1500));

    console.timeEnd("ChartEngine");
    console.log("✅ ChartEngine inicializado\n");
  }

  renderChart(canvas: HTMLCanvasElement, data: number[], color: string) {
    new Chart(canvas, {
      type: "bar",
      data: {
        labels: data.map((_, i) => i + 1),
        datasets: [{ label: "Ventas", data, backgroundColor: color }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
      },
    });
  }
}
