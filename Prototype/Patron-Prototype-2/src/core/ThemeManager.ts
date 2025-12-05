export class ThemeManager {
  async load() {
    console.time("ThemeManager");
    console.log("⏳ Cargando ThemeManager...");

    await new Promise((r) => setTimeout(r, 600));

    const palette = Array.from(
      { length: 2000 },
      (_, i) => `hsl(${i % 360}, 70%, 60%)`
    );

    console.timeEnd("ThemeManager");
    console.log("✅ ThemeManager cargado\n");

    return { palette };
  }
}
