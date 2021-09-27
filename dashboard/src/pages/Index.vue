<template>
   <div class="q-pa-md">
    <q-table
      title="Treats"
      :rows="rows"
      :columns="columns"
      row-key="name"
    />
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageIndex',
  data: () => {
    return {
    rows:[],
    columns : [
  {
    name: 'video_id',
    required: true,
    label: 'Video Id',
    align: 'left',
    field: row => row.video_id,
    
    sortable: true
  },
   { name: 'publish_time', align: 'center', label: 'Publish Time', field: 'publish_time', sortable: true },
   { name: 'title', label: 'Title', field: 'title', sortable: true },
   { name: 'trending_date', align: 'center', label: 'Trending Date', field: 'trending_date', sortable: true },
]}},
 mounted: function () {
   this.getvideosdata();
 }, 
 methods:{
   getvideosdata(){
     this.$axios.get('http://127.0.0.1:5000/').then((response) => {
       if(response.data.ok){
         this.rows=response.data.videos_data
       }
     });
   }   
 }, 
})
</script>
