<template>
  <Card class="p-shadow-7 p-mb-3">
    <template v-slot:content>

      <Inplace :closable="false" :active="state.clicked" v-on:open="handleSwitchStateClicked">
        <template #display>
          <div >
            <h4> {{ state.note }} </h4>
          </div>
        </template>
        <template #content>
          <InputText
            v-model="state.note" autoFocus
          />
        </template>
      </Inplace>

    </template>

    <template v-slot:footer>
      <div class="p-d-flex p-flex-row">
        <Button
            v-if="state.clicked"
            icon="pi pi-check"
            label="Save"
            @click="handleSave"
        />
        <Button
            v-if="state.clicked"
            icon="pi pi-times"
            label="Cancel"
            class="p-button-secondary"
            @click="handleSwitchStateClicked"
        />
        <Button
            icon="pi pi-trash"
            class="p-button-danger"
            label="Delete"
            @click="handleDelete"
        />
      </div>
    </template>
  </Card>
</template>

<script>
  import { reactive } from 'vue';
  import axios from 'axios';

  import Card from 'primevue/card';
  import Inplace from 'primevue/inplace';
  import InputText from 'primevue/inputtext';
  import Button from 'primevue/button';
  import {backend} from "@/utils";

  export default {
    components: {
      Card,
      Inplace,
      InputText,
      Button
    },

    props: {
      id: {
        type: Number,
        required: true,
      },
      note: {
        type: String,
        required: true
      }
    },

    setup(props, { emit }) {
      const state = reactive({
        note: props.note,
        clicked: false,
        submitting: false
      });

      const handleSave = async _ => {
        try {
          state.submitting = true;

          const response = await axios.put(`${backend}/api/note/update/${props.id}`, {
            content: state.note
          }, {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`
            }
          });

          if(response.status === 200) {
            //Success
            emit('ChangedNoteSuccess');
            state.clicked = false;
          }
        } catch(err) {
          const refresh = await axios.post(`${backend}/api/token/refresh/`, { refresh: localStorage.refreshToken });

          localStorage.setItem('accessToken', refresh.data.access);

          const refreshResponse = await axios.put(`${backend}/api/note/update/${props.id}`, {
            content: state.note
          }, {
            headers: {
              Authorization: `Bearer ${refresh.data.access}`
            }
          });

          if(refreshResponse.status === 200) {
            //Success
            emit('ChangedNoteSuccess');
            state.clicked = false;
          }
        } finally {
          state.submitting = false;
        }
      }

      const handleSwitchStateClicked = _ => {
        state.note = props.note;
        state.clicked = !state.clicked;
      }

      const handleDelete = async _ => {
        try {
          state.submitting = true;

          const response = await axios.delete(`${backend}/api/note/delete/${props.id}`, {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`
            }
          });

          if(response.status === 200) {
            emit('removeNote', { id: props.id })
          }
        } catch(err) {
          const refresh = await axios.post(`${backend}/api/token/refresh/`, { refresh: localStorage.refreshToken });

          localStorage.setItem('accessToken', refresh.data.access);

          const refreshResponse = await axios.delete(`${backend}/api/note/delete/${props.id}`, {
            headers: {
              Authorization: `Bearer ${refresh.data.access}`
            }
          });

          if(refreshResponse.status === 200) {
            emit('removeNote', { id: props.id })
          }
        } finally {
          state.submitting = false;
        }

      }

      return {
        state,
        handleSave,
        handleSwitchStateClicked,
        handleDelete
      }
    }
  }
</script>

<style>

</style>
