$(function() {	
$(".table-row-group").on("wb-ready.wb-tables", function (event) {
		$.getScript("/design-system-systeme-conception/backlog/stacked-table/dataTables.rowGroup.min.js", function () {
			$(".table-row-group").each(function () {
				var table = $(this).DataTable();
				new $.fn.dataTable.RowGroup(table);
				var tableCol = $(this).data("wb-tables");
				var colData = tableCol.rowGroup.dataSrc;
				var colOrder = tableCol.rowGroup.orderFixed;
				var colClass = tableCol.rowGroup.className;

				table.rowGroup().order.fixed({
					pre: [colOrder]
				}).dataSrc(colData).draw();

				$(this).on('draw.dt', function () {
$(this).find("tr.group").addClass(colClass);
					$("tr.group").attr("aria-hidden", "true");

				});
				
			});
		});
	});
});
