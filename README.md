# 跨馆巡展的借展可行性与城市排期

本项目保存视觉艺术机构日常业务分析使用的合成演练资料，样例不代表真实机构、作品、交易或研究结论。

## 资料

- `venues.csv`：巡展场馆及场期事实，均为合成演练资料。字段为 `venue_id, city, open_from, open_to, gallery_id, capacity, attendance_source, estimate_basis`。
- `works.csv`：作品条件和休整信息，条件只描述演练记录。字段为 `work_id, medium, display_days_limit, rest_days, required_temp_band, required_light_band, theme_id`。
- `loan_windows.csv`：出借方提供的可借时段和运输要求。字段为 `work_id, lender_id, available_from, available_to, transit_days, environment_note, approval_state`。
- `attendance_history.csv`：既有展期按日期和口径记录的到访事实。字段为 `venue_id, period_start, period_end, visitor_count, measurement, show_type, source_ref`。

记录之间通过 `*_id`、`*_key` 或 `*_ref` 字段关联。日期采用 ISO 格式；空值表示来源未提供该事实，不代表数值为零。不同来源的统计范围和状态以 `docs/data-contract.md` 为准。样例中保留了待确认、取消、缺失和版本变化等原始情况，不包含预先计算的分析结论。

## 运行

需要 Python 3.11 或更高版本，无第三方依赖。运行 `python3 -m unittest discover -s tests -v` 可检查资料编码、字段和记录结构。
