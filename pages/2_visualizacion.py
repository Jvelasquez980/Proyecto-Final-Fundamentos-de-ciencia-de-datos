import streamlit as st
import pandas as pd
import plotly.express as px

from utils.geo import STATE_TO_CODE

st.set_page_config(page_title="Modulo 2 - Visualizacion", layout="wide")

st.title("Modulo 2 - Visualizacion Dinamica")

base_df = st.session_state.get("processed_df")
if base_df is None:
    st.info("Primero procesa los datos en el modulo 1.")
    st.stop()

df = base_df.copy()


date_col = "Order Date" if "Order Date" in df.columns else None
ship_date_col = "Ship Date" if "Ship Date" in df.columns else None

if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
if ship_date_col:
    df[ship_date_col] = pd.to_datetime(df[ship_date_col], errors="coerce")

st.subheader("Filtros globales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if date_col:
        date_min = df[date_col].min()
        date_max = df[date_col].max()
        if pd.notna(date_min) and pd.notna(date_max):
            date_range = st.date_input(
                "Rango de fechas",
                value=(date_min.date(), date_max.date()),
                min_value=date_min.date(),
                max_value=date_max.date(),
            )
        else:
            date_range = None
            st.info("No hay fechas validas para filtrar.")
    else:
        st.info("No hay columna de fecha.")

with col2:
    segment_col = "Segment" if "Segment" in df.columns else None
    segment_values = []
    if segment_col:
        segment_values = sorted(df[segment_col].dropna().unique().tolist())
        selected_segments = st.multiselect(
            "Segmento",
            options=segment_values,
            default=segment_values,
        )
    else:
        selected_segments = []

with col3:
    category_col = "Category" if "Category" in df.columns else None
    category_values = []
    if category_col:
        category_values = sorted(df[category_col].dropna().unique().tolist())
        selected_categories = st.multiselect(
            "Categoria",
            options=category_values,
            default=category_values,
        )
    else:
        selected_categories = []

with col4:
    region_col = "Region" if "Region" in df.columns else None
    region_values = []
    if region_col:
        region_values = sorted(df[region_col].dropna().unique().tolist())
        selected_regions = st.multiselect(
            "Region",
            options=region_values,
            default=region_values,
        )
    else:
        selected_regions = []

col5, col6, col7 = st.columns(3)

with col5:
    subcategory_col = "Sub-Category" if "Sub-Category" in df.columns else None
    subcategory_values = []
    if subcategory_col:
        subcategory_values = sorted(df[subcategory_col].dropna().unique().tolist())
        selected_subcategories = st.multiselect(
            "Subcategoria",
            options=subcategory_values,
            default=subcategory_values,
        )
    else:
        selected_subcategories = []

with col6:
    state_col = "State" if "State" in df.columns else None
    state_values = []
    if state_col:
        state_values = sorted(df[state_col].dropna().unique().tolist())
        selected_states = st.multiselect(
            "Estado",
            options=state_values,
            default=state_values,
        )
    else:
        selected_states = []

with col7:
    city_col = "City" if "City" in df.columns else None
    city_values = []
    if city_col:
        city_values = sorted(df[city_col].dropna().unique().tolist())
        selected_cities = st.multiselect(
            "Ciudad",
            options=city_values,
            default=city_values,
        )
    else:
        selected_cities = []

filtered = df

if date_col:
    if date_range and len(date_range) == 2:
        start_date, end_date = date_range
        filtered = filtered[
            (filtered[date_col] >= pd.Timestamp(start_date))
            & (filtered[date_col] <= pd.Timestamp(end_date))
        ]

if segment_col and selected_segments:
    filtered = filtered[filtered[segment_col].isin(selected_segments)]

if category_col and selected_categories:
    filtered = filtered[filtered[category_col].isin(selected_categories)]

if region_col and selected_regions:
    filtered = filtered[filtered[region_col].isin(selected_regions)]

if subcategory_col and selected_subcategories:
    filtered = filtered[filtered[subcategory_col].isin(selected_subcategories)]

if state_col and selected_states:
    filtered = filtered[filtered[state_col].isin(selected_states)]

if city_col and selected_cities:
    filtered = filtered[filtered[city_col].isin(selected_cities)]

sales_col = "Sales" if "Sales" in filtered.columns else None
profit_col = "Profit" if "Profit" in filtered.columns else None
discount_col = "Discount" if "Discount" in filtered.columns else None
quantity_col = "Quantity" if "Quantity" in filtered.columns else None

if sales_col:
    sales_min = float(filtered[sales_col].min())
    sales_max = float(filtered[sales_col].max())
    sales_range = st.slider(
        "Rango de ventas",
        min_value=sales_min,
        max_value=sales_max,
        value=(sales_min, sales_max),
    )
    filtered = filtered[filtered[sales_col].between(sales_range[0], sales_range[1])]

if profit_col:
    profit_min = float(filtered[profit_col].min())
    profit_max = float(filtered[profit_col].max())
    profit_range = st.slider(
        "Rango de ganancia",
        min_value=profit_min,
        max_value=profit_max,
        value=(profit_min, profit_max),
    )
    filtered = filtered[filtered[profit_col].between(profit_range[0], profit_range[1])]

if filtered.empty:
    st.warning("No hay datos con los filtros actuales.")
    st.stop()

st.session_state["filtered_df"] = filtered

st.subheader("Indicadores clave")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    total_sales = filtered[sales_col].sum() if sales_col else 0
    st.metric("Ventas", f"{total_sales:,.2f}")

with metric2:
    total_profit = filtered[profit_col].sum() if profit_col else 0
    st.metric("Ganancia", f"{total_profit:,.2f}")

with metric3:
    order_col = "Order ID" if "Order ID" in filtered.columns else None
    total_orders = filtered[order_col].nunique() if order_col else len(filtered)
    st.metric("Pedidos", f"{total_orders:,}")

with metric4:
    avg_discount = filtered[discount_col].mean() if discount_col else 0
    st.metric("Descuento promedio", f"{avg_discount:.2%}")

st.subheader("Vista filtrada")
with st.expander("Ver datos filtrados", expanded=False):
    st.dataframe(filtered.head(50), use_container_width=True)

st.divider()

univariado, bivariado, reporte = st.tabs(
    ["Analisis Univariado", "Analisis Bivariado", "Reporte"]
)

with univariado:
    st.write("Distribuciones clave")
    col_a, col_b = st.columns(2)
    with col_a:
        if sales_col:
            fig_sales = px.histogram(filtered, x=sales_col, nbins=40, title="Distribucion de ventas")
            st.plotly_chart(fig_sales, use_container_width=True)
    with col_b:
        if profit_col:
            fig_profit = px.histogram(filtered, x=profit_col, nbins=40, title="Distribucion de ganancia")
            st.plotly_chart(fig_profit, use_container_width=True)

    col_c, col_d = st.columns(2)
    with col_c:
        if discount_col:
            fig_discount = px.box(filtered, y=discount_col, title="Distribucion de descuento")
            st.plotly_chart(fig_discount, use_container_width=True)
    with col_d:
        if quantity_col:
            fig_quantity = px.histogram(filtered, x=quantity_col, nbins=30, title="Distribucion de cantidad")
            st.plotly_chart(fig_quantity, use_container_width=True)

with bivariado:
    st.write("Correlaciones")
    num_cols = filtered.select_dtypes(include="number").columns.tolist()
    col_e, col_f = st.columns(2)
    with col_e:
        if num_cols:
            corr = filtered[num_cols].corr(numeric_only=True)
            fig_corr = px.imshow(corr, text_auto=True, title="Heatmap de correlacion")
            st.plotly_chart(fig_corr, use_container_width=True)

    with col_f:
        st.write("Ventas vs ganancia")
        if sales_col and profit_col:
            color_col = category_col if category_col else None
            fig_scatter = px.scatter(
                filtered,
                x=sales_col,
                y=profit_col,
                color=color_col,
                title="Ventas vs ganancia",
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

with reporte:
    st.write("Evolucion temporal")
    col_g, col_h = st.columns(2)
    with col_g:
        if date_col and sales_col:
            temp = filtered.copy()
            temp = temp.dropna(subset=[date_col])
            temp = temp.sort_values(date_col)
            temp = (
                temp.groupby(pd.Grouper(key=date_col, freq="M"))
                .agg({sales_col: "sum", profit_col: "sum" if profit_col else "sum"})
                .reset_index()
            )
            fig_line = px.line(
                temp,
                x=date_col,
                y=[sales_col, profit_col] if profit_col else [sales_col],
                title="Ventas y ganancia por mes",
            )
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.info("No hay columna de fecha o ventas para la evolucion temporal.")

    with col_h:
        st.write("Top productos por ganancia")
        product_col = "Product Name" if "Product Name" in filtered.columns else None
        if product_col and profit_col:
            top_products = (
                filtered.groupby(product_col)[profit_col]
                .sum()
                .sort_values(ascending=False)
                .head(10)
                .reset_index()
            )
            fig_top = px.bar(
                top_products,
                x=profit_col,
                y=product_col,
                orientation="h",
                title="Top 10 productos por ganancia",
            )
            st.plotly_chart(fig_top, use_container_width=True)
        else:
            st.info("No hay columnas de producto o ganancia.")

    col_i, col_j = st.columns(2)
    with col_i:
        st.write("Mapa por estado (ventas)")
        if state_col and sales_col:
            map_data = (
                filtered.groupby(state_col)[sales_col]
                .sum()
                .reset_index()
                .rename(columns={state_col: "State"})
            )
            map_data["Code"] = map_data["State"].map(STATE_TO_CODE)
            map_data = map_data.dropna(subset=["Code"])
            if not map_data.empty:
                fig_map = px.choropleth(
                    map_data,
                    locations="Code",
                    locationmode="USA-states",
                    color=sales_col,
                    scope="usa",
                    title="Ventas por estado",
                )
                st.plotly_chart(fig_map, use_container_width=True)
            else:
                st.info("No hay estados validos para el mapa.")
        else:
            st.info("No hay columnas de estado o ventas para el mapa.")

    with col_j:
        st.write("Envios por modo")
        ship_mode_col = "Ship Mode" if "Ship Mode" in filtered.columns else None
        if ship_mode_col and sales_col:
            ship_data = (
                filtered.groupby(ship_mode_col)[[sales_col] + ([profit_col] if profit_col else [])]
                .sum()
                .reset_index()
            )
            fig_ship = px.bar(
                ship_data,
                x=ship_mode_col,
                y=[sales_col, profit_col] if profit_col else [sales_col],
                barmode="group",
                title="Ventas y ganancia por modo de envio",
            )
            st.plotly_chart(fig_ship, use_container_width=True)
        else:
            st.info("No hay columnas de modo de envio o ventas.")

    st.write("Resumen estadistico")
    with st.expander("Ver resumen cuantitativo", expanded=False):
        numeric_cols = filtered.select_dtypes(include="number").columns.tolist()
        numeric_cols = [col for col in numeric_cols if col != "Row ID"]
        if numeric_cols:
            st.dataframe(filtered[numeric_cols].describe(), use_container_width=True)
        else:
            st.info("No hay columnas cuantitativas para mostrar.")

    with st.expander("Ver resumen categorico", expanded=False):
        cat_cols = filtered.select_dtypes(include=["object", "category"]).columns.tolist()
        if cat_cols:
            st.dataframe(filtered[cat_cols].describe(), use_container_width=True)
        else:
            st.info("No hay columnas categoricas para mostrar.")
