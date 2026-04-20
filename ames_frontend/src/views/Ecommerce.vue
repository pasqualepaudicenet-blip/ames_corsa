<template>
  <admin-layout>
    <div class="col-12  d-flex justify-content-center">
      <div class=" space-y-6 xl:col-span-7  ">
        <ecommerce-metrics  />
      </div>
      <div class="col-span-12 xl:col-span-5">
        <monthly-sale />
      </div>

      <div class="col-span-12">
        <statistics-chart />
      </div>

      <div class="col-span-12 xl:col-span-5">
        <customer-demographic />
      </div>

      <div class="col-span-12 xl:col-span-7">
        <recent-orders />
      </div>
    </div>
  </admin-layout>
</template>

<script>
import AdminLayout from '../components/layout/AdminLayout.vue'
import EcommerceMetrics from '../components/ecommerce/EcommerceMetrics.vue'
import MonthlyTarget from '../components/ecommerce/MonthlySale.vue'
import MonthlySale from '../components/ecommerce/MonthlyTarget.vue'
import CustomerDemographic from '../components/ecommerce/CustomerDemographic.vue'
import StatisticsChart from '../components/ecommerce/StatisticsChart.vue'
import RecentOrders from '../components/ecommerce/RecentOrders.vue'
export default {
  components: {
    AdminLayout,
    EcommerceMetrics,
    //MonthlyTarget,
    //MonthlySale,
    //CustomerDemographic,
    //StatisticsChart,
    //RecentOrders,
  },
  name: 'Ecommerce',
}
</script>

<style>
.cards-hover:hover{
  transform: scale(1.05);
  cursor: pointer;
}
</style>
