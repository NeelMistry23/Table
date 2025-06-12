<template>
 <q-page class="q-pa-md">
    <q-table
      title="Offices"
      :rows="offices"
      :columns="columns"
      row-key="officeCode"
    >
      <template v-slot:body-cell-officeCode="props">
        <q-td :props="props">
          <q-btn flat color="primary" @click="goToEmployees(props.row.officeCode)">
            {{ props.row.officeCode }}
          </q-btn>
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

import {api} from 'boot/axios'

const offices = ref([])
const router = useRouter()

const columns = [
  { name: 'officeCode', label: 'Office Code', field: 'officeCode' },
  { name: 'city', label: 'City', field: 'city' },
  { name: 'country', label: 'Country', field: 'country' }
]

onMounted(async () => {
  const res = await api.get('/offices')
  offices.value = res.data
})

function goToEmployees(code) {
  router.push(`/offices/${code}/employees`)
}
</script>



