import { ThemeManager } from "../core/ThemeManager";
import { ChartEngine } from "../core/ChartEngine";
import { DataCache } from "../core/DataCache";
import { IPrototype } from "../IPrototype";

export class DashboardWidget implements IPrototype<DashboardWidget> {
  constructor(
    private title: string,
    private type: string,
    private theme: any,
    private chartEngine: ChartEngine,
    private dataCache: any
  ) {}

  static async createPrototype(title: string, type: string) {
    console.time(`Crear Prototipo: ${title}`);
    console.log(`🔧 Creando PROTOTIPO "${title}"...`);

    const themeManager = new ThemeManager();
    const theme = await themeManager.load();

    const chartEngine = new ChartEngine();
    await chartEngine.initialize();

    const dataCache = new DataCache().load();

    console.timeEnd(`Crear Prototipo: ${title}`);
    console.log(`✅ PROTOTIPO "${title}" creado\n`);

    return new DashboardWidget(title, type, theme, chartEngine, dataCache);
  }

  clone(): DashboardWidget {
    console.time(`Clonando ${this.title}`);
    const clone = new DashboardWidget(
      this.title,
      this.type,
      this.theme,
      this.chartEngine,
      this.dataCache
    );
    console.timeEnd(`Clonando ${this.title}`);
    return clone;
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
