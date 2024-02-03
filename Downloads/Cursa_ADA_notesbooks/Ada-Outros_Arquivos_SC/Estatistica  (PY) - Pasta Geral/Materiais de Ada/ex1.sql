with cardio_base_cleaned as (
  select
    cast(age as int) as age,
    cast(gender as int) as gender,
    cast(height as int) as height,
    cast(weight as int) as weight,
    cast(ap_hi as int) as ap_hi,
    cast(ap_lo as int) as ap_lo,
    cast(cholesterol as int) as cholesterol,
    cast(smoke as int) as smoke
  from default.cardio_base
),
cardio_base_age_in_years as (
  select
    *,
    floor(age/365) as age_in_years
  from cardio_base_cleaned
),

cardio_base_grouped_by_age as (
  select
    age_in_years,
    mean(weight) as mean_weight
  from cardio_base_age_in_years
  group by age_in_years
  order by mean_weight desc
),

weight_diff as (
  select
    max(mean_weight) - min(mean_weight)
  from cardio_base_grouped_by_age
)

select * from weight_diff;