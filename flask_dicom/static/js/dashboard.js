/*
 * @Author: Zhao kf
 * @Date: 2021-01-20 11:52:10
 * @LastEditTime: 2021-01-25 02:46:25
 * @LastEditors: Zhao kf
 * @Description: 
 * @FilePath: /dicom_manage/dicom_server/flask_dicom/static/js/dashboard.js
 */
/* globals Chart:false, feather:false */

(function () {
    // 'use strict'
  
    // feather.replace()
  
    // Graphs
    var ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          'Sunday',
          'Monday',
          'Tuesday',
          'Wednesday',
          'Thursday',
          'Friday',
          'Saturday'
        ],
        datasets: [{
          data: [
            15339,
            21345,
            18483,
            24003,
            23489,
            24092,
            12034
          ],
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#007bff',
          borderWidth: 4,
          pointBackgroundColor: '#007bff'
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        },
        legend: {
          display: false
        }
      }
    })
  })()
  
