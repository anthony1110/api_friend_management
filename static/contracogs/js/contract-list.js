"use strict";

function action_formatter(value, row, index) {
    let tpl = _.template('<a class="btn btn-default btn-xs" style="margin-right: 5px" href="<%- url_contract_workflow %>" role="button">View</a>' +
        '<a class="btn btn-default btn-xs" href="<%- url_download_skufile_excel %>" role="button">Download</a>');
    return tpl({
        id: row.id,
        url_contract_workflow: g_url_contract_workflow.replace("999", row.id),
        url_download_skufile_excel: g_url_download_skufile_excel.replace("999", row.id),
        index: index
    });
}

(function ($) {
    function ajax_load_contract_list(params) {
        let data_list = JSON.parse(params.data);

        //Get url parameters
        let url_parameters = _.object(_.compact(_.map(location.search.slice(1).split('&'), function (item) {
            if (item) return item.split('=');
        })));

        if (url_parameters) {
            data_list = Object.assign({}, url_parameters, data_list);
        }

        $.ajax({
            url: g_url_get_contract_list,
            type: "POST",
            data: data_list,
            success: function (data) {
                params.success(data);
            }
        });
    }

    $("#contract-main-table").bootstrapTable({
        ajax: ajax_load_contract_list,
        queryParamsType: "limit",
        queryParams: function (params) {
            params["csrfmiddlewaretoken"] = g_csrf_token;
            return params;
        }
    });
})(jQuery);


$(document).ready(function () {
    $('.datepicker').datepicker();
});
