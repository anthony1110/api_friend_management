"use strict";

function action_formatter(value, row, index) {
    let tpl = _.template('<a class="btn btn-danger btn-xs delete-button" data-toggle="modal" data-id="<%- id %>" data-index="<%- index %>">Delete</a>');
    return tpl({
        id: row.id,
        index: index
    });
}

function final_backmargin_history_formatter(value, row, index) {
    let str_result = '';
    let final_backmargin_histories = row.final_backmargin_history;
    _.each(final_backmargin_histories, function (value, key) {
        if (value) {
            str_result += value.backmargin_value + ' - ' + value.created_at + '<br/>';
        }
    });

    let tpl = _.template(str_result);
    return tpl({});
}

function actual_backmargin_history_formatter(value, row, index) {
    let str_result = '';
    let actual_backmargin_histories = row.actual_backmargin_history;
    _.each(actual_backmargin_histories, function (value, key) {
        if (value) {
            str_result += value.backmargin_value + ' - ' + value.created_at + '<br/>';
        }
    });

    let tpl = _.template(str_result);
    return tpl({});
}

(function ($) {
    function ajax_load_contract_skus(params) {
        let data_list = JSON.parse(params.data);
        $.ajax({
            url: g_url_get_contract_skus,
            type: "POST",
            data: data_list,
            success: function (data) {
                params.success(data);
                // console.log(data);
            }
        });
    }

    function delete_contract_sku(id) {
        $.ajax({
            url: g_url_delete_contract_skus,
            type: "POST",
            data: {
                id: id,
                contract_id: g_contract_id,
                csrfmiddlewaretoken: g_csrf_token
            },
            success: function (data) {
                $("#contract-skus-table").bootstrapTable('refresh', {silent: true});
            }
        });
    }

    $("#contract-skus-table").bootstrapTable({
        ajax: ajax_load_contract_skus,
        queryParamsType: "limit",
        queryParams: function (params) {
            params["country"] = g_country;
            params["contract_id"] = g_contract_id;
            params["csrfmiddlewaretoken"] = g_csrf_token;
            return params;
        }
    });


    $('body').on('click', '.delete-button', function () {
        let contract_id = $(this).data('id');
        if (contract_id) {
            if (confirm('Are you sure you want to remove this SKU from contract?')) {
                delete_contract_sku(contract_id);
            } else {
                // Do nothing!
            }
        }
    });

    // this snippet update the url with tab's hash value so that
    // same tab will be shown when user refresh the page
    let hash = window.location.hash;
    hash && $('ul.nav a[href="' + hash + '"]').tab('show');
    $('.nav-tabs a').click(function (e) {
        $(this).tab('show');
        let scrollmem = $('body').scrollTop() || $('html').scrollTop();
        window.location.hash = this.hash;
        $('html,body').scrollTop(scrollmem);
    });
})(jQuery);

$(document).ready(function () {

});
