import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
  Tooltip,
  Legend
);

const white = "#ffffff";
const valLossRed = "#ef4444";

function LossChart({ logs }) {
  const data = {
    labels: logs.train_loss.map((_, i) => i + 1),
    datasets: [
      {
        label: "Train Loss",
        data: logs.train_loss,
        borderColor: white,
        backgroundColor: "rgba(255, 255, 255, 0.1)",
        borderWidth: 2,
        pointBackgroundColor: white,
        pointBorderColor: white,
        tension: 0.2,
      },
      {
        label: "Val Loss",
        data: logs.val_loss,
        borderColor: valLossRed,
        backgroundColor: "rgba(239, 68, 68, 0.15)",
        borderWidth: 2,
        pointBackgroundColor: valLossRed,
        pointBorderColor: valLossRed,
        tension: 0.2,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        labels: {
          color: white,
          font: { size: 12 },
        },
      },
      tooltip: {
        titleColor: white,
        bodyColor: white,
        backgroundColor: "rgba(15, 23, 42, 0.95)",
        borderColor: "rgba(255, 255, 255, 0.3)",
        borderWidth: 1,
      },
    },
    scales: {
      x: {
        grid: { color: "rgba(255, 255, 255, 0.15)" },
        ticks: { color: white, font: { size: 11 } },
      },
      y: {
        grid: { color: "rgba(255, 255, 255, 0.15)" },
        ticks: { color: white, font: { size: 11 } },
      },
    },
  };

  return <Line data={data} options={options} />;
}

export default LossChart;
