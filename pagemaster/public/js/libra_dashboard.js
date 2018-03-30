document.addEventListener("DOMContentLoaded", function(){
	if (frappe.csrf_token != "None") {
		$("#not-permitted").toggle();
		if (!frappe.content) {
			// ToDo: Outsource this script in own .js and load dynamicly direct in .html for each record in dashboard doctype...
			$("#example").toggle();
			chartMixed();		
			
			/* let chart = new Chart( "#chart", { // or DOM element
				data: {
					// ToDo: replace variales with jinja
					labels: ["12am-3am", "3am-6am", "6am-9am", "9am-12pm", "12pm-3pm", "3pm-6pm", "6pm-9pm", "9pm-12am"],
					datasets: [
						{
							name: "Some Data", type: 'bar',
							values: [25, 40, 30, 35, 8, 52, 17, -4]
						},
						{
							name: "Another Set", type: 'bar',
							values: [25, 50, -10, 15, 18, 32, 27, 14]
						},
						{
							name: "Yet Another", type: 'line',
							values: [15, 20, -3, -15, 58, 12, -17, 37]
						}
					],
					yMarkers: [{ label: "Marker", value: 70 }],
					yRegions: [{ label: "Region", start: -10, end: 50 }]
				},
				title: "My Awesome Chart",
				type: "axis-mixed", // or 'bar', 'line', 'pie', 'percentage'
				height: 250,
				colors: ['purple', '#ffa3ef', 'red']
			}); */
		}
	}
});

function chartMixed() {
	let typeData = {
	labels: ["12am-3am", "3am-6am", "6am-9am", "9am-12pm",
		"12pm-3pm", "3pm-6pm", "6pm-9pm", "9pm-12am"],

	yMarkers: [
		{
			label: "Marker",
			value: 43,
			// type: 'dashed'
		}
	],

	yRegions: [
		{
			label: "Region",
			start: -10,
			end: 50
		},
	],

	datasets: [
		{
			name: "Some Data",
			values: [18, 40, 30, 35, 8, 52, 17, -4],
			axisPosition: 'right',
			chartType: 'bar'
		},
		{
			name: "Another Set",
			values: [30, 50, -10, 15, 18, 32, 27, 14],
			axisPosition: 'right',
			chartType: 'bar'
		},
		{
			name: "Yet Another",
			values: [15, 20, -3, -15, 58, 12, -17, 37],
			chartType: 'line'
		}
	]
};



let args = {
	data: typeData,
	type: 'axis-mixed',
	height: 500,
	colors: ['purple', 'magenta', 'light-blue'],

	maxLegendPoints: 6,
	maxSlices: 10,

	tooltipOptions: {
		formatTooltipX: d => (d + '').toUpperCase(),
		formatTooltipY: d => d + ' pts',
	}
}
let aggrChart = new Chart("#chart", args);
}