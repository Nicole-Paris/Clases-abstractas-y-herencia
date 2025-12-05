export class DataCache {
  load() {
    console.time("DataCache");
    console.log("⏳ Cargando DataCache...");

    const data = Array.from({ length: 50 }, () => ({
      ventas: Math.floor(Math.random() * 100),
    }));

    console.timeEnd("DataCache");
    console.log("✅ DataCache cargado\n");

    return data;
  }
}
