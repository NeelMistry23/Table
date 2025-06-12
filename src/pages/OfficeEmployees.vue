<template>
  <q-page class="q-pa-md">
    <q-btn label="Back" icon="arrow_back" @click="goBack" flat />

    <q-table
      title="Employees"
      :rows="employees"
      :columns="columns"
      row-key="employeeNumber"
      class="q-mt-md"
    />

    <q-btn label="Add Employee" color="primary" @click="showDialog = true" class="q-mt-md" />

    <q-dialog v-model="showDialog">
      <q-card style="min-width: 300px">
        <q-card-section>
          <div class="text-h6">Add New Employee</div>
        </q-card-section>

        <q-card-section>
          <q-input v-model="form.firstName" label="First Name" dense />
          <q-input v-model="form.lastName" label="Last Name" dense />
          <q-input v-model="form.extension" label="Extension" dense />
          <q-input v-model="form.email" label="Email" type="email" dense />
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Save" color="primary" @click="saveEmployee" />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>


<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useQuasar } from 'quasar'

const route = useRoute()
const router = useRouter()
const $q = useQuasar()

const officeCode = route.params.officeCode
const employees = ref([])
const showDialog = ref(false)

const form = ref({
  firstName: '',
  lastName: '',
  extension: '',
  email: ''
})

const columns = [
  { name: 'employeeNumber', label: 'Emp No', field: 'employeeNumber' },
  { name: 'firstName', label: 'First Name', field: 'firstName' },
  { name: 'lastName', label: 'Last Name', field: 'lastName' },
  { name: 'email', label: 'Email', field: 'email' }
]

async function fetchEmployees() {
  const res = await axios.get(`http://localhost:5000/api/get_office_employees/${officeCode}/`)
  employees.value = res.data
}

function goBack() {
  router.push('/')
}

async function saveEmployee() {
  try {
    const res = await axios.post(`http://localhost:5000/api/new_employee/${officeCode}/`, form.value)
    if (res.data.ok) {
      $q.notify({ type: 'positive', message: 'Employee added successfully' })
      showDialog.value = false
      fetchEmployees()
    } else {
      $q.notify({ type: 'negative', message: res.data.error || 'Error adding employee' })
    }
  } catch (err) {
    $q.notify({ type: 'negative', message: err.message })
  }
}

onMounted(fetchEmployees)
</script>





