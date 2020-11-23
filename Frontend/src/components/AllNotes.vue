<template>
  <div v-if="state.loading">
    <h1> Loading... </h1>
  </div>
  <div v-else>
    <div class="p-mt-2 p-text-left" style="padding: 1em;">
      <h1> Your notes </h1>
      <h4> You can view, edit and delete all of your notes here! </h4>
    </div>

    <Note
        v-for="note in state.notes"
        :id="note.id"
        :note="note.content"
        @removeNote="handleRemoveNote"
        @ChangedNoteSuccess="ChangedNoteSuccess"
    />
  </div>

  <Toast />
</template>

<script>
  import { reactive, onMounted } from 'vue';
  import axios from 'axios';
  import Note from '../components/Note';
  import { backend } from "@/utils";
  import router from "@/router";

  import Toast from 'primevue/toast';
  import { useToast } from 'primevue/usetoast';

  export default {
    components: {
      Note,
      Toast
    },
    name: 'AllNotes',
    setup() {
      const toast = useToast();

      const state = reactive({
        loading: true,
        notes: []
      });

      // We get all the notes for the user
      const getNotes = async _ => {
        try {
          const response = await axios.get(`${backend}/api/user/notes`, {
            headers: {
              Authorization: `Bearer ${localStorage.accessToken}`
            }
          });

          if(response.status === 200) {
            state.notes = response.data;
          }
        } catch(err) {
          if(err.status === 500) {
            //Throw error
          } else {
            try {
              const refresh = await axios.post(`${backend}/api/token/refresh/`, { refresh: localStorage.refreshToken });

              localStorage.setItem('accessToken', refresh.data.access);

              const refreshResponse = await axios.get(`${backend}/api/user/notes`, {
                headers: {
                  Authorization: `Bearer ${refresh.data.access}`
                }
              });

              if(refreshResponse.status === 200) {
                state.notes = refreshResponse.data;
              }
            } catch {
              localStorage.removeItem('accessToken');
              localStorage.removeItem('refreshToken');

              await router.push({ name: 'Login' });
            }
          }
        } finally {
          state.loading = false;
        }
      }

      onMounted(() => {
        getNotes();
      });

      // Note component sends us the Id of the deleted note and we just remove
      // it from the list
      const handleRemoveNote = childData => state.notes = state.notes.filter(note => note.id !== childData.id );

      const ChangedNoteSuccess = _ => {
        toast.add({ severity:'success', summary: 'Saved!', detail:'Changes you made are saved!', life: 3000 });
      }

      return {
        state,
        handleRemoveNote,
        ChangedNoteSuccess
      }
    }
  }
</script>

<style scoped>

</style>
