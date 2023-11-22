DROP PROCEDURE IF EXISTS sp_DBR_restaurant_webservice
$$
CREATE PROCEDURE `sp_DBR_restaurant_webservice`()
BEGIN
  DECLARE intId int;
  DECLARE restaurantMinimumAge int;
  set intId = CAST(@id AS UNSIGNED);
  IF( intId = 0 OR @id is null  ) THEN
    set intId = 25309;
  END IF;
  
  
set @attr_id_name = sf_AHA_get_attribute_id('name', 'catalog_product');
set @attr_id_short_description =  sf_AHA_get_attribute_id('short_description', 'catalog_product');
set @attr_id_description =  sf_AHA_get_attribute_id('description', 'catalog_product');
set @attr_id_weight =  sf_AHA_get_attribute_id('weight', 'catalog_product');
set @attr_id_status = sf_AHA_get_attribute_id('status', 'catalog_product');
set @attr_id_price = sf_AHA_get_attribute_id('price', 'catalog_product');
set @attr_id_special_price = sf_AHA_get_attribute_id('special_price', 'catalog_product');
set @attr_id_special_from_date = sf_AHA_get_attribute_id('special_from_date', 'catalog_product');
set @attr_id_special_to_date = sf_AHA_get_attribute_id('special_to_date', 'catalog_product');
set @attr_id_restaurant_opening_time = sf_AHA_get_attribute_id('restaurant_opening_time', 'catalog_product');
set @attr_id_restaurant_opening_time = sf_AHA_get_attribute_id('restaurant_opening_time', 'catalog_product');
set @attr_id_restaurant_open_date = sf_AHA_get_attribute_id('restaurant_open_date', 'catalog_product');
set @attr_id_restaurant_menu =  sf_AHA_get_attribute_id('restaurant_menu', 'catalog_product');
set @attr_id_image = sf_AHA_get_attribute_id('image', 'catalog_product');
set @attr_id_overlay_url = sf_AHA_get_attribute_id('overlay_url', 'catalog_product');
set @attr_id_text_banner = sf_AHA_get_attribute_id('text_banner', 'catalog_product');
set @attr_id_bestselling_rank =  sf_AHA_get_attribute_id('bestselling_rank', 'catalog_product');
set @attr_id_restaurant_address =  sf_AHA_get_attribute_id('restaurant_address', 'catalog_product');
set @attr_id_restaurant_delivery_postcodes =  sf_AHA_get_attribute_id('restaurant_delivery_postcodes', 'catalog_product');
set @attr_id_allergy_info = sf_AHA_get_attribute_id('allergy_info', 'catalog_product');
set @attr_prep_time = sf_AHA_get_attribute_id('restaurant_cooking_time', 'catalog_product');
set @attr_id_min_preorder_delay = sf_AHA_get_attribute_id('minimum_preorder_delay', 'catalog_product');
set @attr_id_last_order_min = sf_AHA_get_attribute_id('restaurant_last_order_min', 'catalog_product');
set @attr_id_ingredients = sf_AHA_get_attribute_id('ingredients', 'catalog_product');
set @attr_id_location = sf_AHA_get_attribute_id('restaurant_location', 'catalog_product');
set @attr_id_product_variables = sf_AHA_get_attribute_id('product_variables', 'catalog_product');
set @attr_id_restaurant_cooking_time =  sf_AHA_get_attribute_id('cooking_time', 'catalog_product');
set @attr_id_restaurant_delivery_time =  sf_AHA_get_attribute_id('restaurant_delivery_time', 'catalog_product');
set @attr_id_hide_same_as_last =  sf_AHA_get_attribute_id('hide_same_as_last', 'catalog_product');
set @attr_id_option_group =  sf_AHA_get_attribute_id('restaurant_option_group', 'catalog_product');
set @attr_id_restaurant_start_order_min = sf_AHA_get_attribute_id('restaurant_start_order_min', 'catalog_product');
set @attr_id_minimum_age = sf_AHA_get_attribute_id('minimum_age', 'catalog_product');
set @attr_id_media_gallery = sf_AHA_get_attribute_id('media_gallery', 'catalog_product');
-- Get restaurant minimum_age
SELECT minimum_age.value as minimum_age
into restaurantMinimumAge
from AhaProdDB.catalog_product_entity e
  left join AhaProdDB.catalog_product_entity_int minimum_age
    on minimum_age.entity_id = e.entity_id and minimum_age.attribute_id = @attr_id_minimum_age and minimum_age.store_id = 0
WHERE e.entity_id = intId;
select default_value into @default_allergy_info  from AhaProdDB.eav_attribute where attribute_code = 'allergy_info';
  select plain_value into @delivery_time from AhaProdDB.core_variable v
  inner join  AhaProdDB.core_variable_value vv on v.variable_id = vv.variable_id
  where code = 'delivery_time';
  
   select plain_value into @driver_distance_times from AhaProdDB.core_variable v
  inner join AhaProdDB.core_variable_value vv on vv.variable_id = v.variable_id
  where code = 'driver_wait_times';
select e.entity_id,
    e.sku,
    name.value as name,
    short.value as short_description,
    description.value as description,
    IF(english.product_id is null, 0, 1) english,
    IF(ename.value is null, name.value ,ename.value) as english_name,
    IF(eshort.value is null, short.value ,eshort.value) as english_short_description,
    IF(edescription.value is null, description.value ,edescription.value) as english_description,
    price.value as price,
    special.value as special_price,
    image.value as image,
    overlay_url.value as overlay_url,
    text_banner.value as text_banner,
    e_text_banner.value as english_text_banner,
    open.value as open_days,
    open.value as restaurant_opening_time,
    open_dates.value as open_dates,
    status.value as status,
    address.value as address,
    location.value as location,
    cooking_time.value as cooking_time,
    IF( address.value like '%800 Selfoss%', 25,
      -- GREATEST(delivery_time.value, @delivery_time)
      ROUND(IFNULL(GREATEST((JSON_EXTRACT(@driver_distance_times, CONCAT('$."', e.entity_id, '"')) / 60) * 1.2, 10, @delivery_time - 5),25), 0)
    ) as delivery_time,
    prep_time.value as prep_time,
    attribute_set_name,
    rating.reviews_count,
    rating.rating_summary as rating,
    hide_same_as_last.value as hide_same_as_last,
    mpd.value as minimum_preorder_delay,
    last_order_min.value as last_order_time,
    GREATEST(30, delivery_time.value -10, @delivery_time -10) as last_delivery_order_time,
    IFNULL(allergy_info.value, @default_allergy_info) as allergy_info,
    IFNULL(en_allergy_info.value, IFNULL(allergy_info.value, @default_allergy_info)) as en_allergy_info,
 --   substring_index(product_vars.value, 'min_max_preparation_time', -1) mm,
    restaurant_start_order_min.value as restaurant_start_order_min,
   -- minimum_age.value as minimum_age
    restaurantMinimumAge as minimum_age
    
from AhaProdDB.catalog_product_entity e 
inner join AhaProdDB.catalog_product_entity_varchar name on name.entity_id = e.entity_id and name.attribute_id = @attr_id_name and name.store_id = 0
inner join AhaProdDB.eav_attribute_set a on a.attribute_set_id = e.attribute_set_id
left join AhaProdDB.catalog_product_entity_text short on short.entity_id = e.entity_id and short.attribute_id = @attr_id_short_description and short.store_id = 0
left join AhaProdDB.catalog_product_entity_text description on description.entity_id = e.entity_id and description.attribute_id = @attr_id_description and short.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar ename on ename.entity_id = e.entity_id and ename.attribute_id = @attr_id_name and ename.store_id = 2
left join AhaProdDB.catalog_product_entity_text eshort on eshort.entity_id = e.entity_id and eshort.attribute_id = @attr_id_short_description and eshort.store_id = 2
inner join AhaProdDB.catalog_product_entity_int status on status.entity_id = e.entity_id and status.attribute_id = @attr_id_status  and status.store_id = 0
left join AhaProdDB.catalog_product_entity_decimal price on price.entity_id = e.entity_id and price.attribute_id = @attr_id_price and price.store_id = 0
left join AhaProdDB.catalog_product_entity_decimal special on special.entity_id = e.entity_id and special.attribute_id =  @attr_id_special_price and special.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar image on image.entity_id = e.entity_id and image.attribute_id = @attr_id_image and image.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar overlay_url on overlay_url.entity_id = e.entity_id and overlay_url.attribute_id = @attr_id_overlay_url and overlay_url.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar text_banner on text_banner.entity_id = e.entity_id and text_banner.attribute_id = @attr_id_text_banner and text_banner.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar e_text_banner on e_text_banner.entity_id = e.entity_id and e_text_banner.attribute_id = @attr_id_text_banner and e_text_banner.store_id = 2
left join AhaProdDB.catalog_product_entity_text product_vars on product_vars.entity_id = e.entity_id and product_vars.attribute_id = @attr_id_product_variables and product_vars.store_id = 0
left join AhaProdDB.catalog_product_entity_text open on open.entity_id = e.entity_id and open.attribute_id = @attr_id_restaurant_opening_time and open.store_id = 0
left join AhaProdDB.catalog_product_entity_text open_dates on open_dates.entity_id = e.entity_id and open_dates.attribute_id = @attr_id_restaurant_open_date and open_dates.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar last_order_min on open_dates.entity_id = e.entity_id and last_order_min.attribute_id = @attr_id_last_order_min and last_order_min.store_id = 0
left join AhaProdDB.catalog_product_entity_text address on address.entity_id = e.entity_id and address.attribute_id = @attr_id_restaurant_address
left join AhaProdDB.catalog_product_entity_varchar location on location.entity_id = e.entity_id and location.attribute_id = @attr_id_location and location.store_id = 0
left join AhaProdDB.catalog_product_entity_text mpd on mpd.entity_id = e.entity_id and mpd.attribute_id = @attr_id_min_preorder_delay
left join AhaProdDB.catalog_product_entity_varchar cooking_time on cooking_time.entity_id = e.entity_id and cooking_time.attribute_id = @attr_id_restaurant_cooking_time
left join AhaProdDB.catalog_product_entity_varchar prep_time on prep_time.entity_id = e.entity_id and prep_time.attribute_id = @attr_prep_time
left join AhaProdDB.catalog_product_entity_varchar delivery_time on delivery_time.entity_id = e.entity_id and delivery_time.attribute_id = @attr_id_restaurant_delivery_time
left join AhaProdDB.catalog_product_entity_int hide_same_as_last on hide_same_as_last.entity_id = e.entity_id and hide_same_as_last.attribute_id = @attr_id_hide_same_as_last  and hide_same_as_last.store_id = 0
left join AhaProdDB.catalog_product_enabled_index english on english.product_id = e.entity_id and english.store_id = 2
left join AhaProdDB.review_entity_summary rating on rating.entity_pk_value = e.entity_id
left join AhaProdDB.catalog_product_entity_text allergy_info on allergy_info.entity_id = e.entity_id and allergy_info.attribute_id = @attr_id_allergy_info and allergy_info.store_id = 0
left join AhaProdDB.catalog_product_entity_text en_allergy_info on en_allergy_info.entity_id = e.entity_id and en_allergy_info.attribute_id = @attr_id_allergy_info and en_allergy_info.store_id = 2
left join AhaProdDB.catalog_product_entity_varchar restaurant_start_order_min on restaurant_start_order_min.entity_id = e.entity_id and restaurant_start_order_min.attribute_id = @attr_id_restaurant_start_order_min and restaurant_start_order_min.store_id = 0
-- left join AhaProdDB.catalog_product_entity_int minimum_age on minimum_age.entity_id = e.entity_id and minimum_age.attribute_id = @attr_id_minimum_age and minimum_age.store_id = 0
where e.entity_id = intId
and name.store_id = 0
and status.value = 1
and status.store_id = 0
group by e.entity_id
order by status.value, sku;
set @overwrite = '';
IF( intId in (25151,25153,25154,391111,25309,25311,488681) ) THEN
  set @overwrite = 'overwrite:w_150,c_pad';
END IF;
-- Restaurant items
select e.entity_id,
    e.sku,
    -- name.value as name,
    IF(pflat.entity_id is null, CONCAT("Væntanlegt - ", name.value), name.value) as name,
    short.value as short_description,
    ingredients.value as ingredients,
    
    -- opv.value as menu_category,
    IF(iopv.value is null, opv.value ,iopv.value) as menu_category,
    op.sort_order as menu_order,
    bestselling_rank.value as br,
    IF(english.product_id is null, 0, 1) english,
    IF(ename.value is null, name.value ,ename.value) as english_name,
    IF(eshort.value is null, short.value ,eshort.value) as english_short_description,
    IF(eingredients.value is null, ingredients.value ,eingredients.value) as en_ingredients,
    IF(eopv.value is null, opv.value ,eopv.value) as english_menu_category,
    delivery_postcodes.value as delivery_postcodes,
    price.value as price,
    special.value as special_price,
    special_from_date.value as special_price_from,
    special_to_date.value as special_price_to,
    image.value as image,
    IF( media_value.label is null OR TRIM(media_value.label) = '', @overwrite, media_value.label) as image_label,
    overlay_url.value as overlay_url,
    text_banner.value as text_banner,
    e_text_banner.value as english_text_banner,
    open.value as restricted_time,
    open_dates.value as restricted_dates,
    mpd.value as minimum_preorder_delay,
    status.value as status,
    attribute_set_name,
    e.has_options,
    ogv.value as option_group,
    IFNULL(minimum_age.value, restaurantMinimumAge) as minimum_age
from AhaProdDB.catalog_product_link l
inner join AhaProdDB.catalog_product_entity e on e.entity_id = l.linked_product_id
inner join AhaProdDB.catalog_product_entity_varchar name on name.entity_id = e.entity_id and name.attribute_id = @attr_id_name and name.store_id = 0
inner join AhaProdDB.eav_attribute_set a on a.attribute_set_id = e.attribute_set_id
left join AhaProdDB.catalog_product_flat_1 pflat on pflat.entity_id = e.entity_id 
left join AhaProdDB.catalog_product_link_attribute_int position on l.link_id = position.link_id and position.product_link_attribute_id = 7
left join AhaProdDB.catalog_product_entity_text short on short.entity_id = e.entity_id and short.attribute_id = @attr_id_short_description and short.store_id = 0
left join AhaProdDB.catalog_product_entity_text ingredients on ingredients.entity_id = e.entity_id and ingredients.attribute_id = @attr_id_ingredients and ingredients.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar ename on ename.entity_id = e.entity_id and ename.attribute_id = @attr_id_name and ename.store_id = 2
left join AhaProdDB.catalog_product_entity_text eshort on eshort.entity_id = e.entity_id and eshort.attribute_id = @attr_id_short_description and eshort.store_id = 2
left join AhaProdDB.catalog_product_entity_text eingredients on eingredients.entity_id = e.entity_id and eingredients.attribute_id = @attr_id_ingredients and eingredients.store_id = 2
inner join AhaProdDB.catalog_product_entity_int status on status.entity_id = e.entity_id and status.attribute_id = @attr_id_status  and status.store_id = 0
left join AhaProdDB.catalog_product_entity_decimal price on price.entity_id = e.entity_id and price.attribute_id = @attr_id_price and price.store_id = 0
left join AhaProdDB.catalog_product_entity_decimal special on special.entity_id = e.entity_id and special.attribute_id =  @attr_id_special_price and special.store_id = 0
left join AhaProdDB.catalog_product_entity_datetime special_from_date on special_from_date.entity_id = e.entity_id and special_from_date.attribute_id =  @attr_id_special_from_date and special_from_date.store_id = 0
left join AhaProdDB.catalog_product_entity_datetime special_to_date on special_to_date.entity_id = e.entity_id and special_to_date.attribute_id =  @attr_id_special_to_date and special_to_date.store_id = 0
left join AhaProdDB.catalog_product_entity_decimal weight on weight.entity_id = e.entity_id and weight.attribute_id =  @attr_id_weight 
left join AhaProdDB.catalog_product_entity_varchar image on image.entity_id = e.entity_id and image.attribute_id = @attr_id_image
left join AhaProdDB.catalog_product_entity_media_gallery media
  inner join AhaProdDB.catalog_product_entity_media_gallery_value media_value
     ON media.value_id = media_value.value_id 
ON media.entity_id = e.entity_id and media.attribute_id = @attr_id_media_gallery and media.value = image.value
    
left join AhaProdDB.catalog_product_entity_varchar overlay_url on overlay_url.entity_id = e.entity_id and overlay_url.attribute_id = @attr_id_overlay_url and overlay_url.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar text_banner on text_banner.entity_id = e.entity_id and text_banner.attribute_id = @attr_id_text_banner and text_banner.store_id = 0
left join AhaProdDB.catalog_product_entity_varchar e_text_banner on e_text_banner.entity_id = e.entity_id and e_text_banner.attribute_id = @attr_id_text_banner and e_text_banner.store_id = 2
left join AhaProdDB.catalog_product_entity_text open on open.entity_id = e.entity_id and open.attribute_id = @attr_id_restaurant_opening_time and open.store_id = 0
left join AhaProdDB.catalog_product_entity_text open_dates on open_dates.entity_id = e.entity_id and open_dates.attribute_id = @attr_id_restaurant_open_date and open_dates.store_id = 0
left join AhaProdDB.catalog_product_entity_text mpd on mpd.entity_id = e.entity_id and mpd.attribute_id = @attr_id_min_preorder_delay
left join AhaProdDB.catalog_product_entity_varchar delivery_postcodes on delivery_postcodes.entity_id = e.entity_id and delivery_postcodes.attribute_id = @attr_id_restaurant_delivery_postcodes
left join AhaProdDB.catalog_product_entity_int menu_category on menu_category.entity_id = e.entity_id and menu_category.attribute_id = @attr_id_restaurant_menu and menu_category.store_id = 0
left join AhaProdDB.eav_attribute_option op on op.attribute_id = @attr_id_restaurant_menu and op.option_id = menu_category.value
left join AhaProdDB.eav_attribute_option_value opv on opv.option_id = op.option_id and opv.store_id = 0
left join AhaProdDB.eav_attribute_option_value iopv on iopv.option_id = op.option_id and iopv.store_id = 1
left join AhaProdDB.eav_attribute_option_value eopv on eopv.option_id = op.option_id and eopv.store_id = 2
left join AhaProdDB.catalog_product_entity_int bestselling_rank on bestselling_rank.entity_id = e.entity_id and bestselling_rank.attribute_id = @attr_id_bestselling_rank
left join AhaProdDB.catalog_product_entity_int option_group on option_group.entity_id = e.entity_id and option_group.attribute_id = @attr_id_option_group and option_group.store_id = 0
left join AhaProdDB.eav_attribute_option og on og.attribute_id = @attr_id_option_group and og.option_id = option_group.value
left join AhaProdDB.eav_attribute_option_value ogv on ogv.option_id = og.option_id and ogv.store_id = 0
left join AhaProdDB.catalog_product_enabled_index english on english.product_id = e.entity_id and english.store_id = 2
left join AhaProdDB.catalog_product_entity_int minimum_age on minimum_age.entity_id = e.entity_id and minimum_age.attribute_id = @attr_id_minimum_age and minimum_age.store_id = 0
where l.product_id = intId
and l.link_type_id = 3
and name.store_id = 0
and status.store_id = 0
and status.value = 1
 and (ogv.value is null or ogv.value not in('plastic_bags_required'))
order by status.value, op.sort_order, position.value desc, bestselling_rank.value desc;
select opv.option_id as menu_category_id,
    -- opv.value as menu_category,
    IF(iopv.value is null, opv.value ,iopv.value) as menu_category,
    op.sort_order as menu_order,
    IF(eopv.value is null, opv.value ,eopv.value) as english_menu_category,
    count(*) as count,
    status.value status
from AhaProdDB.catalog_product_link l
inner join AhaProdDB.catalog_product_entity e on e.entity_id = l.linked_product_id
inner join AhaProdDB.eav_attribute_set a on a.attribute_set_id = e.attribute_set_id
inner join AhaProdDB.catalog_product_entity_int status on status.entity_id = e.entity_id and status.attribute_id = @attr_id_status  and status.store_id = 0
left join AhaProdDB.catalog_product_entity_int menu_category on menu_category.entity_id = e.entity_id and menu_category.attribute_id = @attr_id_restaurant_menu
left join AhaProdDB.eav_attribute_option op on op.attribute_id = @attr_id_restaurant_menu and op.option_id = menu_category.value
left join AhaProdDB.eav_attribute_option_value opv on opv.option_id = op.option_id and opv.store_id = 0
left join AhaProdDB.eav_attribute_option_value iopv on iopv.option_id = op.option_id and iopv.store_id = 1
left join AhaProdDB.eav_attribute_option_value eopv on eopv.option_id = op.option_id and eopv.store_id = 2
left join AhaProdDB.catalog_product_entity_int option_group on option_group.entity_id = e.entity_id and option_group.attribute_id = @attr_id_option_group and option_group.store_id = 0
left join AhaProdDB.eav_attribute_option og on og.attribute_id = @attr_id_option_group and og.option_id = option_group.value
left join AhaProdDB.eav_attribute_option_value ogv on ogv.option_id = og.option_id and ogv.store_id = 0
where l.product_id = intId
and l.link_type_id = 3
and status.store_id = 0
and status.value = 1
and opv.option_id is not null
and (ogv.value is null or ogv.value not in('plastic_bags_required'))
group by menu_category_id
order by menu_order;
END
$$