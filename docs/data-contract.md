# 合成资料约定

资料用于本地业务流程演练，字段仅记录事实来源，不预先裁定业务结果。

- `venues.csv`：巡展场馆及场期事实，均为合成演练资料。字段为 `venue_id, city, open_from, open_to, gallery_id, capacity, attendance_source, estimate_basis`。
- `works.csv`：作品条件和休整信息，条件只描述演练记录。字段为 `work_id, medium, display_days_limit, rest_days, required_temp_band, required_light_band, theme_id`。
- `loan_windows.csv`：出借方提供的可借时段和运输要求。字段为 `work_id, lender_id, available_from, available_to, transit_days, environment_note, approval_state`。
- `attendance_history.csv`：既有展期按日期和口径记录的到访事实。字段为 `venue_id, period_start, period_end, visitor_count, measurement, show_type, source_ref`。

空字段表示事实尚未提供，`pending`、`review`、`hold` 等状态表示来源记录尚未形成最终确认。不同来源以事件日期或有效期表达的时间含义不相同，调用方应结合表名和字段解释；不能仅因编号相同就假定两条记录可合并。金额以资料中记载的名义单位表示，没有统一换算或预先扣除退款。
