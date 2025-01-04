
Descriptive Statistics ReportToggle navigation[Descriptive Statistics Report](#top)* [Overview](#overview)
* [Variables](#variables-dropdown)
* [Correlations](#correlations_tab)
* [Missing values](#missing)
* [Sample](#sample)
Overview
========

Brought to you by [YData](https://ydata.ai/?utm_source=opensource&utm_medium=ydataprofiling&utm_campaign=report)

* [Overview](#overview-dataset_overview)
* [Alerts 11](#overview-alerts)
* [Reproduction](#overview-reproduction)

Dataset statistics



| Number of variables | 9 |
| --- | --- |
| Number of observations | 5 |
| Missing cells | 0 |
| Missing cells (%) | 0\.0% |
| Duplicate rows | 0 |
| Duplicate rows (%) | 0\.0% |
| Total size in memory | 759\.0 B |
| Average record size in memory | 151\.8 B |

Variable types



| Text | 1 |
| --- | --- |
| Categorical | 8 |



Alerts

| [`Day 7`](#pp_var_-1827597381412283182) has constant value "0" | Constant |
| [`Day 1`](#pp_var_4628463023654373478) is highly overall correlated with `Day 2` and 2 other fields | High correlation |
| [`Day 2`](#pp_var_2396086430972043885) is highly overall correlated with `Day 1` and 2 other fields | High correlation |
| [`Day 3`](#pp_var_2248215345274481087) is highly overall correlated with `Day 1` and 3 other fields | High correlation |
| [`Day 4`](#pp_var_-1605438763001897838) is highly overall correlated with `Day 6` and 1 other fields | High correlation |
| [`Day 5`](#pp_var_4258496501754609882) is highly overall correlated with `Day 6` and 1 other fields | High correlation |
| [`Day 6`](#pp_var_7865001069477510313) is highly overall correlated with `Day 3` and 3 other fields | High correlation |
| [`Total`](#pp_var_4725598794279154534) is highly overall correlated with `Day 1` and 5 other fields | High correlation |
| [`Total`](#pp_var_4725598794279154534) is uniformly distributed | Uniform |
| [`Map`](#pp_var_7073590953944671367) has unique values | Unique |
| [`Total`](#pp_var_4725598794279154534) has unique values | Unique |

Reproduction



| Analysis started | 2024\-09\-14 03:06:15\.126014 |
| --- | --- |
| Analysis finished | 2024\-09\-14 03:06:15\.851381 |
| Duration | 0\.73 seconds |
| Software version | [ydata\-profiling vv4\.10\.0](https://github.com/ydataai/ydata-profiling) |
| Download configuration | [config.json](data:text/plain;charset=utf-8,%7B%22title%22%3A%20%22Descriptive%20Statistics%20Report%22%2C%20%22dataset%22%3A%20%7B%22description%22%3A%20%22%22%2C%20%22creator%22%3A%20%22%22%2C%20%22author%22%3A%20%22%22%2C%20%22copyright_holder%22%3A%20%22%22%2C%20%22copyright_year%22%3A%20%22%22%2C%20%22url%22%3A%20%22%22%7D%2C%20%22variables%22%3A%20%7B%22descriptions%22%3A%20%7B%7D%7D%2C%20%22infer_dtypes%22%3A%20true%2C%20%22show_variable_description%22%3A%20true%2C%20%22pool_size%22%3A%200%2C%20%22progress_bar%22%3A%20true%2C%20%22vars%22%3A%20%7B%22num%22%3A%20%7B%22quantiles%22%3A%20%5B0.05%2C%200.25%2C%200.5%2C%200.75%2C%200.95%5D%2C%20%22skewness_threshold%22%3A%2020%2C%20%22low_categorical_threshold%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%7D%2C%20%22text%22%3A%20%7B%22length%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22redact%22%3A%20false%7D%2C%20%22cat%22%3A%20%7B%22length%22%3A%20true%2C%20%22characters%22%3A%20true%2C%20%22words%22%3A%20true%2C%20%22cardinality_threshold%22%3A%2050%2C%20%22percentage_cat_threshold%22%3A%200.5%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22n_obs%22%3A%205%2C%20%22chi_squared_threshold%22%3A%200.999%2C%20%22coerce_str_to_date%22%3A%20false%2C%20%22redact%22%3A%20false%2C%20%22histogram_largest%22%3A%2050%2C%20%22stop_words%22%3A%20%5B%5D%7D%2C%20%22image%22%3A%20%7B%22active%22%3A%20true%2C%20%22exif%22%3A%20true%2C%20%22hash%22%3A%20true%7D%2C%20%22bool%22%3A%20%7B%22n_obs%22%3A%203%2C%20%22imbalance_threshold%22%3A%200.5%2C%20%22mappings%22%3A%20%7B%22t%22%3A%20true%2C%20%22f%22%3A%20false%2C%20%22yes%22%3A%20true%2C%20%22no%22%3A%20false%2C%20%22y%22%3A%20true%2C%20%22n%22%3A%20false%2C%20%22true%22%3A%20true%2C%20%22false%22%3A%20false%7D%7D%2C%20%22path%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22file%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22url%22%3A%20%7B%22active%22%3A%20true%7D%2C%20%22timeseries%22%3A%20%7B%22active%22%3A%20false%2C%20%22sortby%22%3A%20null%2C%20%22autocorrelation%22%3A%200.7%2C%20%22lags%22%3A%20%5B1%2C%207%2C%2012%2C%2024%2C%2030%5D%2C%20%22significance%22%3A%200.05%2C%20%22pacf_acf_lag%22%3A%20100%7D%7D%2C%20%22sort%22%3A%20null%2C%20%22missing_diagrams%22%3A%20%7B%22bar%22%3A%20true%2C%20%22matrix%22%3A%20true%2C%20%22heatmap%22%3A%20true%7D%2C%20%22correlation_table%22%3A%20true%2C%20%22correlations%22%3A%20%7B%22auto%22%3A%20%7B%22key%22%3A%20%22auto%22%2C%20%22calculate%22%3A%20true%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22spearman%22%3A%20%7B%22key%22%3A%20%22spearman%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22pearson%22%3A%20%7B%22key%22%3A%20%22pearson%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22phi_k%22%3A%20%7B%22key%22%3A%20%22phi_k%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22cramers%22%3A%20%7B%22key%22%3A%20%22cramers%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%2C%20%22kendall%22%3A%20%7B%22key%22%3A%20%22kendall%22%2C%20%22calculate%22%3A%20false%2C%20%22warn_high_correlations%22%3A%2010%2C%20%22threshold%22%3A%200.5%2C%20%22n_bins%22%3A%2010%7D%7D%2C%20%22interactions%22%3A%20%7B%22continuous%22%3A%20true%2C%20%22targets%22%3A%20%5B%5D%7D%2C%20%22categorical_maximum_correlation_distinct%22%3A%20100%2C%20%22memory_deep%22%3A%20true%2C%20%22plot%22%3A%20%7B%22missing%22%3A%20%7B%22force_labels%22%3A%20true%2C%20%22cmap%22%3A%20%22RdBu%22%7D%2C%20%22image_format%22%3A%20%22svg%22%2C%20%22correlation%22%3A%20%7B%22cmap%22%3A%20%22RdBu%22%2C%20%22bad%22%3A%20%22%23000000%22%7D%2C%20%22dpi%22%3A%20800%2C%20%22histogram%22%3A%20%7B%22bins%22%3A%2050%2C%20%22max_bins%22%3A%20250%2C%20%22x_axis_labels%22%3A%20true%2C%20%22density%22%3A%20false%7D%2C%20%22scatter_threshold%22%3A%201000%2C%20%22cat_freq%22%3A%20%7B%22show%22%3A%20true%2C%20%22type%22%3A%20%22bar%22%2C%20%22max_unique%22%3A%2010%2C%20%22colors%22%3A%20null%7D%2C%20%22font_path%22%3A%20null%7D%2C%20%22duplicates%22%3A%20%7B%22head%22%3A%2010%2C%20%22key%22%3A%20%22%23%20duplicates%22%7D%2C%20%22samples%22%3A%20%7B%22head%22%3A%2010%2C%20%22tail%22%3A%2010%2C%20%22random%22%3A%200%7D%2C%20%22reject_variables%22%3A%20true%2C%20%22n_obs_unique%22%3A%2010%2C%20%22n_freq_table_max%22%3A%2010%2C%20%22n_extreme_obs%22%3A%2010%2C%20%22report%22%3A%20%7B%22precision%22%3A%208%7D%2C%20%22html%22%3A%20%7B%22style%22%3A%20%7B%22primary_colors%22%3A%20%5B%22%23377eb8%22%2C%20%22%23e41a1c%22%2C%20%22%234daf4a%22%5D%2C%20%22logo%22%3A%20%22%22%2C%20%22theme%22%3A%20null%7D%2C%20%22navbar_show%22%3A%20true%2C%20%22minify_html%22%3A%20true%2C%20%22use_local_assets%22%3A%20true%2C%20%22inline%22%3A%20true%2C%20%22assets_prefix%22%3A%20null%2C%20%22assets_path%22%3A%20null%2C%20%22full_width%22%3A%20false%7D%2C%20%22notebook%22%3A%20%7B%22iframe%22%3A%20%7B%22height%22%3A%20%22800px%22%2C%20%22width%22%3A%20%22100%25%22%2C%20%22attribute%22%3A%20%22srcdoc%22%7D%7D%7D) |

Variables
=========

Select ColumnsMapTotalDay 1Day 2Day 3Day 4Day 5Day 6Day 7[Map](#pp_var_7073590953944671367)  
Text

`UNIQUE`  



| Distinct | 5 |
| --- | --- |
| Distinct (%) | 100\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 439\.0 B |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:15\.954516image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ More details * [Overview](#7073590953944671367bottom-7073590953944671367overview)
* [Words](#7073590953944671367bottom-7073590953944671367word)
* [Characters](#7073590953944671367bottom-7073590953944671367characters)

Length



| Max length | 6 |
| --- | --- |
| Median length | 5 |
| Mean length | 5\.2 |
| Min length | 4 |

Characters and Unicode



| Total characters | 26 |
| --- | --- |
| Distinct characters | 19 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 5 ? |
| --- | --- |
| Unique (%) | 100\.0% |

Sample



| 1st row | Ascent |
| --- | --- |
| 2nd row | Bind |
| 3rd row | Haven |
| 4th row | Icebox |
| 5th row | Split |



| Value | Count | Frequency (%) |
| --- | --- | --- |
| ascent | 1 | 20\.0% |
| bind | 1 | 20\.0% |
| haven | 1 | 20\.0% |
| icebox | 1 | 20\.0% |
| split | 1 | 20\.0% |

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:16\.381818image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/* [Characters](#7073590953944671367unicode-7073590953944671367characters)
* [Categories](#7073590953944671367unicode-7073590953944671367categories)
* [Scripts](#7073590953944671367unicode-7073590953944671367scripts)
* [Blocks](#7073590953944671367unicode-7073590953944671367blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 26 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| e | 3 | 11\.5% |
| n | 3 | 11\.5% |
| c | 2 | 7\.7% |
| t | 2 | 7\.7% |
| i | 2 | 7\.7% |
| A | 1 | 3\.8% |
| I | 1 | 3\.8% |
| p | 1 | 3\.8% |
| S | 1 | 3\.8% |
| x | 1 | 3\.8% |
| Other values (9\) | 9 | 34\.6% |

[Total](#pp_var_4725598794279154534)  
Categorical

`HIGH CORRELATION`  `UNIFORM`  `UNIQUE`  



| Distinct | 5 |
| --- | --- |
| Distinct (%) | 100\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 419\.0 B |



| 2 | 1 |
| --- | --- |
| 9 | 1 |
| 3 | 1 |
| 8 | 1 |
| 12 | 1 |

 More details * [Overview](#4725598794279154534bottom-4725598794279154534overview)
* [Categories](#4725598794279154534bottom-4725598794279154534string)
* [Words](#4725598794279154534bottom-4725598794279154534word)
* [Characters](#4725598794279154534bottom-4725598794279154534characters)

Length



| Max length | 2 |
| --- | --- |
| Median length | 1 |
| Mean length | 1\.2 |
| Min length | 1 |

Characters and Unicode



| Total characters | 6 |
| --- | --- |
| Distinct characters | 5 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 5 ? |
| --- | --- |
| Unique (%) | 100\.0% |

Sample



| 1st row | 2 |
| --- | --- |
| 2nd row | 9 |
| 3rd row | 3 |
| 4th row | 8 |
| 5th row | 12 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 1 | 20\.0% |
| 9 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |
| 8 | 1 | 20\.0% |
| 12 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:16\.593841image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:16\.770756image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 1 | 20\.0% |
| 9 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |
| 8 | 1 | 20\.0% |
| 12 | 1 | 20\.0% |

* [Characters](#4725598794279154534unicode-4725598794279154534characters)
* [Categories](#4725598794279154534unicode-4725598794279154534categories)
* [Scripts](#4725598794279154534unicode-4725598794279154534scripts)
* [Blocks](#4725598794279154534unicode-4725598794279154534blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 6 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 6 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 6 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 33\.3% |
| 9 | 1 | 16\.7% |
| 3 | 1 | 16\.7% |
| 8 | 1 | 16\.7% |
| 1 | 1 | 16\.7% |

[Day 1](#pp_var_4628463023654373478)  
Categorical

`HIGH CORRELATION`  



| Distinct | 4 |
| --- | --- |
| Distinct (%) | 80\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 2 |
| --- | --- |
| 2 | 1 |
| 1 | 1 |
| 3 | 1 |

 More details * [Overview](#4628463023654373478bottom-4628463023654373478overview)
* [Categories](#4628463023654373478bottom-4628463023654373478string)
* [Words](#4628463023654373478bottom-4628463023654373478word)
* [Characters](#4628463023654373478bottom-4628463023654373478characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 4 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 3 ? |
| --- | --- |
| Unique (%) | 60\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 2 |
| 3rd row | 0 |
| 4th row | 1 |
| 5th row | 3 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:16\.962000image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:17\.126205image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

* [Characters](#4628463023654373478unicode-4628463023654373478characters)
* [Categories](#4628463023654373478unicode-4628463023654373478categories)
* [Scripts](#4628463023654373478unicode-4628463023654373478scripts)
* [Blocks](#4628463023654373478unicode-4628463023654373478blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

[Day 2](#pp_var_2396086430972043885)  
Categorical

`HIGH CORRELATION`  



| Distinct | 4 |
| --- | --- |
| Distinct (%) | 80\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 2 |
| --- | --- |
| 3 | 1 |
| 1 | 1 |
| 2 | 1 |

 More details * [Overview](#2396086430972043885bottom-2396086430972043885overview)
* [Categories](#2396086430972043885bottom-2396086430972043885string)
* [Words](#2396086430972043885bottom-2396086430972043885word)
* [Characters](#2396086430972043885bottom-2396086430972043885characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 4 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 3 ? |
| --- | --- |
| Unique (%) | 60\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 3 |
| 3rd row | 0 |
| 4th row | 1 |
| 5th row | 2 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:17\.309435image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:17\.475475image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

* [Characters](#2396086430972043885unicode-2396086430972043885characters)
* [Categories](#2396086430972043885unicode-2396086430972043885categories)
* [Scripts](#2396086430972043885unicode-2396086430972043885scripts)
* [Blocks](#2396086430972043885unicode-2396086430972043885blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 3 | 1 | 20\.0% |
| 1 | 1 | 20\.0% |
| 2 | 1 | 20\.0% |

[Day 3](#pp_var_2248215345274481087)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 1 | 3 |
| --- | --- |
| 0 | 1 |
| 3 | 1 |

 More details * [Overview](#2248215345274481087bottom-2248215345274481087overview)
* [Categories](#2248215345274481087bottom-2248215345274481087string)
* [Words](#2248215345274481087bottom-2248215345274481087word)
* [Characters](#2248215345274481087bottom-2248215345274481087characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 2 ? |
| --- | --- |
| Unique (%) | 40\.0% |

Sample



| 1st row | 1 |
| --- | --- |
| 2nd row | 1 |
| 3rd row | 1 |
| 4th row | 0 |
| 5th row | 3 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:17\.659143image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:17\.817768image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

* [Characters](#2248215345274481087unicode-2248215345274481087characters)
* [Categories](#2248215345274481087unicode-2248215345274481087categories)
* [Scripts](#2248215345274481087unicode-2248215345274481087scripts)
* [Blocks](#2248215345274481087unicode-2248215345274481087blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 3 | 60\.0% |
| 0 | 1 | 20\.0% |
| 3 | 1 | 20\.0% |

[Day 4](#pp_var_-1605438763001897838)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 2 | 2 |
| --- | --- |
| 1 | 2 |
| 0 | 1 |

 More details * [Overview](#-1605438763001897838bottom--1605438763001897838overview)
* [Categories](#-1605438763001897838bottom--1605438763001897838string)
* [Words](#-1605438763001897838bottom--1605438763001897838word)
* [Characters](#-1605438763001897838bottom--1605438763001897838characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 1 ? |
| --- | --- |
| Unique (%) | 20\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 2 |
| 3rd row | 1 |
| 4th row | 2 |
| 5th row | 1 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:17\.993813image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:18\.151561image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

* [Characters](#-1605438763001897838unicode--1605438763001897838characters)
* [Categories](#-1605438763001897838unicode--1605438763001897838categories)
* [Scripts](#-1605438763001897838unicode--1605438763001897838scripts)
* [Blocks](#-1605438763001897838unicode--1605438763001897838blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 2 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

[Day 5](#pp_var_4258496501754609882)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 1 | 2 |
| --- | --- |
| 2 | 2 |
| 0 | 1 |

 More details * [Overview](#4258496501754609882bottom-4258496501754609882overview)
* [Categories](#4258496501754609882bottom-4258496501754609882string)
* [Words](#4258496501754609882bottom-4258496501754609882word)
* [Characters](#4258496501754609882bottom-4258496501754609882characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 1 ? |
| --- | --- |
| Unique (%) | 20\.0% |

Sample



| 1st row | 1 |
| --- | --- |
| 2nd row | 1 |
| 3rd row | 0 |
| 4th row | 2 |
| 5th row | 2 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:18\.327816image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:18\.487321image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

* [Characters](#4258496501754609882unicode-4258496501754609882characters)
* [Categories](#4258496501754609882unicode-4258496501754609882categories)
* [Scripts](#4258496501754609882unicode-4258496501754609882scripts)
* [Blocks](#4258496501754609882unicode-4258496501754609882blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 1 | 2 | 40\.0% |
| 2 | 2 | 40\.0% |
| 0 | 1 | 20\.0% |

[Day 6](#pp_var_7865001069477510313)  
Categorical

`HIGH CORRELATION`  



| Distinct | 3 |
| --- | --- |
| Distinct (%) | 60\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 2 |
| --- | --- |
| 1 | 2 |
| 2 | 1 |

 More details * [Overview](#7865001069477510313bottom-7865001069477510313overview)
* [Categories](#7865001069477510313bottom-7865001069477510313string)
* [Words](#7865001069477510313bottom-7865001069477510313word)
* [Characters](#7865001069477510313bottom-7865001069477510313characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 3 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 1 ? |
| --- | --- |
| Unique (%) | 20\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 0 |
| 3rd row | 1 |
| 4th row | 2 |
| 5th row | 1 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:18\.661645image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:18\.821598image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

* [Characters](#7865001069477510313unicode-7865001069477510313characters)
* [Categories](#7865001069477510313unicode-7865001069477510313categories)
* [Scripts](#7865001069477510313unicode-7865001069477510313scripts)
* [Blocks](#7865001069477510313unicode-7865001069477510313blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 2 | 40\.0% |
| 1 | 2 | 40\.0% |
| 2 | 1 | 20\.0% |

[Day 7](#pp_var_-1827597381412283182)  
Categorical

`CONSTANT`  



| Distinct | 1 |
| --- | --- |
| Distinct (%) | 20\.0% |
| Missing | 0 |
| Missing (%) | 0\.0% |
| Memory size | 418\.0 B |



| 0 | 5 |
| --- | --- |

 More details * [Overview](#-1827597381412283182bottom--1827597381412283182overview)
* [Categories](#-1827597381412283182bottom--1827597381412283182string)
* [Words](#-1827597381412283182bottom--1827597381412283182word)
* [Characters](#-1827597381412283182bottom--1827597381412283182characters)

Length



| Max length | 1 |
| --- | --- |
| Median length | 1 |
| Mean length | 1 |
| Min length | 1 |

Characters and Unicode



| Total characters | 5 |
| --- | --- |
| Distinct characters | 1 |
| Distinct categories | 1 [?](https://en.wikipedia.org/wiki/Unicode_character_property#General_Category "Unicode categories (click for more information)") |
| Distinct scripts | 1 [?](https://en.wikipedia.org/wiki/Script_(Unicode)#List_of_scripts_in_Unicode "Unicode scripts (click for more information)") |
| Distinct blocks | 1 [?](https://en.wikipedia.org/wiki/Unicode_block "Unicode blocks (click for more information)") |

 The Unicode Standard assigns character properties to each code point, which can be used to analyse textual variables. Unique



| Unique | 0 ? |
| --- | --- |
| Unique (%) | 0\.0% |

Sample



| 1st row | 0 |
| --- | --- |
| 2nd row | 0 |
| 3rd row | 0 |
| 4th row | 0 |
| 5th row | 0 |

#### Common Values



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Length

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:18\.995944image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Histogram of lengths of the category #### Common Values (Plot)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:19\.144968image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

* [Characters](#-1827597381412283182unicode--1827597381412283182characters)
* [Categories](#-1827597381412283182unicode--1827597381412283182categories)
* [Scripts](#-1827597381412283182unicode--1827597381412283182scripts)
* [Blocks](#-1827597381412283182unicode--1827597381412283182blocks)

#### Most occurring characters



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Most occurring categories



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per category

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Most occurring scripts



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per script

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

#### Most occurring blocks



| Value | Count | Frequency (%) |
| --- | --- | --- |
| (unknown) | 5 | 100\.0% |

#### Most frequent character per block

##### *(unknown)*



| Value | Count | Frequency (%) |
| --- | --- | --- |
| 0 | 5 | 100\.0% |

Correlations
============

* [Auto](#correlations_tab-auto_diagram_table)

* [Heatmap](#auto_diagram_table-auto_diagram)
* [Table](#auto_diagram_table-auto_table)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:19\.249122image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/

|  | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Day 1 | 1\.000 | 1\.000 | 0\.816 | 0\.000 | 0\.000 | 0\.000 | 1\.000 |
| Day 2 | 1\.000 | 1\.000 | 0\.816 | 0\.000 | 0\.000 | 0\.000 | 1\.000 |
| Day 3 | 0\.816 | 0\.816 | 1\.000 | 0\.000 | 0\.000 | 0\.577 | 1\.000 |
| Day 4 | 0\.000 | 0\.000 | 0\.000 | 1\.000 | 0\.000 | 0\.500 | 1\.000 |
| Day 5 | 0\.000 | 0\.000 | 0\.000 | 0\.000 | 1\.000 | 0\.500 | 1\.000 |
| Day 6 | 0\.000 | 0\.000 | 0\.577 | 0\.500 | 0\.500 | 1\.000 | 1\.000 |
| Total | 1\.000 | 1\.000 | 1\.000 | 1\.000 | 1\.000 | 1\.000 | 1\.000 |

Missing values
==============

* [Count](#missing-bar)
* [Matrix](#missing-matrix)

xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:15\.445650image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ A simple visualization of nullity by column. xml version\="1\.0" encoding\="utf\-8" standalone\="no"?
2024\-09\-14T03:06:15\.761928image/svg\+xmlMatplotlib v3\.7\.5, https://matplotlib.org/ Nullity matrix is a data\-dense display which lets you quickly visually pick out patterns in data completion. Sample
======

* [First rows](#sample-head)
* [Last rows](#sample-tail)



|  | Map | Total | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Ascent | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | Bind | 9 | 2 | 3 | 1 | 2 | 1 | 0 | 0 |
| 2 | Haven | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 3 | Icebox | 8 | 1 | 1 | 0 | 2 | 2 | 2 | 0 |
| 4 | Split | 12 | 3 | 2 | 3 | 1 | 2 | 1 | 0 |



|  | Map | Total | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 | Day 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Ascent | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | Bind | 9 | 2 | 3 | 1 | 2 | 1 | 0 | 0 |
| 2 | Haven | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 3 | Icebox | 8 | 1 | 1 | 0 | 2 | 2 | 2 | 0 |
| 4 | Split | 12 | 3 | 2 | 3 | 1 | 2 | 1 | 0 |

Report generated by [YData](https://ydata.ai/?utm_source=opensource&utm_medium=pandasprofiling&utm_campaign=report).

