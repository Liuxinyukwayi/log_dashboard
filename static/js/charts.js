// static/js/charts.js

document.addEventListener("DOMContentLoaded", function () {
    loadErrorChart();
});

function loadErrorChart() {
    fetch('/api/error_count')
        .then(res => res.json())
        .then(data => {
            const chartDom = document.getElementById('errorChart');
            const myChart = echarts.init(chartDom);
            const option = {
                title: {
                    text: '错误日志数量'
                },
                tooltip: {},
                xAxis: {
                    type: 'category',
                    data: ['过去1小时']
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    name: '错误数',
                    type: 'bar',
                    data: [data.error_count]
                }]
            };
            myChart.setOption(option);
        })
        .catch(err => console.error('加载图表失败:', err));
}

function searchLogs() {
    const keyword = document.getElementById('keyword').value;

    fetch('/api/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ keyword })
    })
        .then(res => res.json())
        .then(data => {
            const logsDiv = document.getElementById('logs');
            if (data.length === 0) {
                logsDiv.textContent = '未找到相关日志。';
            } else {
                logsDiv.textContent = data.map(hit => hit._source.message || JSON.stringify(hit._source)).join('\n\n');
            }
        })
        .catch(err => {
            document.getElementById('logs').textContent = '查询失败。';
            console.error(err);
        });
}
