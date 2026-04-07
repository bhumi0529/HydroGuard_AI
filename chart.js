import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
);

function Chart({ data }) {
  const chartData = {
    labels: data.map((_, index) => "Test " + (index + 1)),
    datasets: [
      {
        label: "Groundwater",
        data: data.map(item => item.groundwater),
        borderWidth: 2,
      },
      {
        label: "Rainfall",
        data: data.map(item => item.rainfall),
        borderWidth: 2,
      },
      {
        label: "Temperature",
        data: data.map(item => item.temperature),
        borderWidth: 2,
      },
    ],
  };

  return (
    <div>
      <h3>📊 Groundwater Trend</h3>
      <Line data={chartData} />
    </div>
  );
}

export default Chart;