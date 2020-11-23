<template>
  <div class="p-fluid">
    <div class="p-mt-2 p-text-left" style="padding: 1em;">
      <h1> Create a note </h1>
      <h4> Notes can be used as reminders, important things you did in your life or anything else in between </h4>
    </div>
    <div class="p-field">
      <label for="note">Note:</label>
      <Textarea
          id="note"
          v-model="state.note"
          :class="state.noteError ? 'p-error' : null"
      />
    </div>

    <div>
      <Button
          :class="state.submitting ? 'p-disabled' : null"
          @click="handleAddNote"
          label="Add Note"
      />
    </div>
    <Toast />
  </div>
</template>

<script>
  import { reactive, computed } from 'vue';
  import axios from 'axios';

  import Button from 'primevue/button';
  import Textarea from 'primevue/textarea';
  import Toast from 'primevue/toast';

  import { useToast } from 'primevue/usetoast';

  import { backend } from '@/utils';
  import router from "@/router";

  export default {
    name: 'CreateNote',
    components: {
      Button,
      Textarea,
      Toast
    },
    setup() {
      const toast = useToast();

      const state = reactive({
        note: null,
        noteError: computed(() => {
          const text = state.note;

          return text === null || text.length > 512;
        }),

        submitting: false,
      })

      const handleAddNote = async _ => {
        if(!state.noteError) {
          // For the loading effect
          state.submitting = true;

          try {
            // I get the initial response
            // If it fails then i need to send the refresh token and try again
            // If it fails again then that means the refresh token expired and i can
            // log out the user
            const response = await axios.post(`${backend}/api/note/create`, { content: state.note }, {
              headers: {
                Authorization: `Bearer ${localStorage.accessToken}`
              }
            });

            if (response.status === 200) {
              toast.add({ severity:'success', summary: 'Success!', detail:'Note is added!', life: 3000 });
              state.note = null
            }
          } catch(err) {
            if(err.status === 500) {
              toast.add({ severity:'error', summary: 'Error!', detail:'Check your internet connection!', life: 3000 });
            } else {
              try {
                const refresh = await axios.post(`${backend}/api/token/refresh/`, { refresh: localStorage.refreshToken });

                await localStorage.setItem('accessToken', refresh.data.access);

                const refreshResponse =  await axios.post(`${backend}/api/note/create`, { content: state.note }, {
                  headers: {
                    Authorization: `Bearer ${localStorage.accessToken}`
                  }
                });

                if (refreshResponse.status === 200) {
                  toast.add({ severity:'success', summary: 'Success!', detail:'Note is added!', life: 3000 });
                  state.note = null
                }
              } catch(err) {
                localStorage.removeItem('accessToken');
                localStorage.removeItem('refreshToken');

                await router.push({ name: 'Login' });
              }
            }
          } finally {
            state.submitting = false;
          }
        }
      }

      return {
        state,
        handleAddNote
      }
    }
  }
</script>

<style scoped>

</style>
