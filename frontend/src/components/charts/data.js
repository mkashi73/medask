import { $themeColors } from '@themeConfig'
// colors
const chartColors = {
  primaryColorShade: '#836AF9',
  yellowColor: '#ffe800',
  successColorShade: '#28dac6',
  warningColorShade: '#ffe802',
  warningLightColor: '#FDAC34',
  infoColorShade: '#299AFF',
  greyColor: '#4F5D70',
  blueColor: '#2c9aff',
  blueLightColor: '#84D0FF',
  greyLightColor: '#EDF1F4',
  tooltipShadow: 'rgba(0, 0, 0, 0.25)',
  lineChartPrimary: '#666ee8',
  lineChartDanger: '#ff4961',
  labelColor: '#6e6b7b',
  grid_line_color: 'rgba(200, 200, 200, 0.2)',
}

export default {

  polarChart: {
    options: {
      responsive: true,
      maintainAspectRatio: false,
      responsiveAnimationDuration: 500,
      legend: {
        position: 'right',
        labels: {
          usePointStyle: true,
          padding: 25,
          boxWidth: 10,
          fontColor: chartColors.labelColor,
        },
      },
      tooltips: {
        // Updated default tooltip UI
        shadowOffsetX: 1,
        shadowOffsetY: 1,
        shadowBlur: 8,
        shadowColor: chartColors.tooltipShadow,
        backgroundColor: $themeColors.light,
        titleFontColor: $themeColors.dark,
        bodyFontColor: $themeColors.dark,
      },
      scale: {
        scaleShowLine: true,
        scaleLineWidth: 1,
        ticks: {
          display: false,
          fontColor: chartColors.labelColor,
        },
        reverse: false,
        gridLines: {
          display: false,
        },
      },
      animation: {
        animateRotate: false,
      },
    },
    data: {
      labels: ['Africa', 'Asia', 'Europe', 'America', 'Antarctica', 'Australia'],
      datasets: [
        {
          label: 'Population (millions)',
          backgroundColor: [
            chartColors.primaryColorShade,
            chartColors.warningColorShade,
            $themeColors.primary,
            chartColors.infoColorShade,
            chartColors.greyColor,
            chartColors.successColorShade,
          ],
          data: [19, 17.5, 15, 13.5, 11, 9],
          borderWidth: 0,
        },
      ],
    },
  },
}