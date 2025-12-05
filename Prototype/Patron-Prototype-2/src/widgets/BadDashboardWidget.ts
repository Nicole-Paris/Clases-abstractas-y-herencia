import { ThemeManager } from "../core/ThemeManager";
import { ChartEngine } from "../core/ChartEngine";
import { DataCache } from "../core/DataCache";

export class BadDashboardWidget {
  constructor(
    private title: string,
    private type: string,
    private theme: any,
    private chartEngine: ChartEngine,
    private dataCache: any
  ) {}

  static async create(title: string, type: string) {
    console.time(`Crear Widget (sin Prototype): ${title}`);
    console.log(`🔧 Creando "${title}" SIN Prototype...`);

    const themeManager = new ThemeManager();
    const theme = await themeManager.load();

    const chartEngine = new ChartEngine();
    await chartEngine.initialize();

    const dataCache = new DataCache().load();

    console.timeEnd(`Crear Widget (sin Prototype): ${title}`);
    console.log(`✅ Widget "${title}" creado\n`);

    return new BadDashboardWidget(title, type, theme, chartEngine, dataCache);
  }

  render(container: HTMLElement, index: number) {
    const widget = document.createElement("div");
    widget.className = "widget";

    const color = this.theme.palette[(index * 10) % this.theme.palette.length];

    widget.innerHTML = `<h3>${this.title} #${index + 1}</h3><canvas></canvas>`;
    container.appendChild(widget);

    const canvas = widget.querySelector("canvas") as HTMLCanvasElement;
    const data = this.dataCache.map((d: any) => d.ventas);

    this.chartEngine.renderChart(canvas, data, color);
  }
}
