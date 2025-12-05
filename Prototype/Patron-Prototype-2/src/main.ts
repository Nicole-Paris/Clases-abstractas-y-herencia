import { DashboardWidget } from "./widgets/DashboardWidget";
import { BadDashboardWidget } from "./widgets/BadDashboardWidget";

const dashboard = document.getElementById("dashboard")!;
const btnWithout = document.getElementById("btnWithout")!;
const btnWith = document.getElementById("btnWith")!;

btnWithout.addEventListener("click", async () => {
  dashboard.innerHTML = "";
  console.clear();
  console.log("=== ❌ SIN PROTOTYPE ===");
  console.time("Total sin Prototype");

  const w1 = await BadDashboardWidget.create("Reporte Q1", "Bar");
  const w2 = await BadDashboardWidget.create("Reporte Q2", "Line");
  const w3 = await BadDashboardWidget.create("Reporte Q3", "Pie");

  [w1, w2, w3].forEach((w, i) => w.render(dashboard, i));

  console.timeEnd("Total sin Prototype");
});

btnWith.addEventListener("click", async () => {
  dashboard.innerHTML = "";
  console.clear();
  console.log("=== ✅ CON PROTOTYPE ===");
  console.time("Total con Prototype");

  const prototype = await DashboardWidget.createPrototype(
    "Prototipo Base",
    "Dashboard"
  );
  const clones = [prototype.clone(), prototype.clone(), prototype.clone()];

  clones.forEach((w, i) => w.render(dashboard, i));

  console.timeEnd("Total con Prototype");
});
