<template>
  <div>
    <div class="p-d-flex p-flex-column p-flex-md-row">
      <div class="p-fluid form">

        <h2 class="p-mb-4"> Login to Notes </h2>

        <div class="p-field p-grid p-a-center">
          <label for="username" class="p-col-12">Username: </label>
          <div class="p-col-12">
            <InputText
                id="username"
                type="text"
                class="p-inputtext-lg"
                :class="state.usernameError ? 'p-invalid' : null"
                v-model="state.username"
            />
          </div>
        </div>

        <div class="p-field p-grid">
          <label for="password" class="p-col-12">Password: </label>
          <div class="p-col-12">
          <span class="p-input-icon-right">
            <InputText
                id="password"
                :type="state.hiddenPassword ? 'password' : 'text'"
                class="p-inputtext-lg"
                :class="state.passwordError ? 'p-invalid' : null"
                v-model="state.password"
            />
            <i v-if="state.hiddenPassword" class="pi pi-eye icon" @click="handlePasswordView" />
            <i v-else class="pi pi-eye-slash icon" @click="handlePasswordView" />
          </span>
          </div>
        </div>

        <div class="p-field p-grid">
          <small id="account">Don't have an account ? <router-link to="/signup"> Click here </router-link> to sign up! </small>
        </div>

        <div>
          <Button
              @click="handleLogin"
              label="Log in"
          />
        </div>
      </div>
      <div style="height: 100vh; width: 100%; background-color: #883cae" class="p-d-none p-d-md-inline-flex">
        <div style="color: white; text-align: center; display: block; margin: 16em auto auto auto">
          <h1> NOTES </h1>
          <h2 class="p-mt-2"> Login to the best notes app on the net!</h2>
          <h3 class="p-mt-2"> Add notes and edit notes to organize yourself better </h3>
        </div>
      </div>
    </div>
    </div>
    <Toast/>
</template>

<script>
  import axios from 'axios';
  import { reactive, computed } from 'vue';

  import Button from 'primevue/button';
  import InputText from 'primevue/inputtext';
  import Toast from 'primevue/toast';

  import { useToast } from 'primevue/usetoast';

  import { backend } from '@/utils';
  import router from '@/router';

  export default {
    components: {
      Button,
      InputText,
      Toast
    },

    setup() {
      const toast = useToast();

      if(localStorage.getItem('accessToken') || localStorage.getItem('refreshToken')) {
        router.push({ name: 'Home' })
      }

      const state = reactive({
        username: null,
        usernameError: computed(() => {
          if(state.username) {
            const text = state.username;

            return text.length < 4;
          }
        }),

        password: null,
        passwordError: computed(() => {
          if(state.password) {
            const text = state.password;

            return text.length < 4;
          }
        }),

        hiddenPassword: true,

        submitted: false
      });

      const handlePasswordView = _ => state.hiddenPassword = !state.hiddenPassword

      const handleLogin = async _ => {
        if(!state.usernameError && !state.passwordError) {
          state.submitted = true;

          try {
            const response = await axios.post(`${backend}/api/token/`, {
              username: state.username,
              password: state.password
            });

            if (response.status === 200) {
              localStorage.setItem('accessToken', response.data.access);
              localStorage.setItem('refreshToken', response.data.refresh);

              await router.push({ name: 'Home' });
            }

            toast.add({ severity:'success', summary: 'Welcome!', detail:'', life: 3000 });
          } catch(err) {
            if(err.status === 401) {
              toast.add({ severity:'error', summary: 'Error!', detail:'Check your credentials!', life: 3000 });
            } else {
              toast.add({ severity:'error', summary: 'Error!', detail:'Check your internet connection!', life: 3000 });
            }
          } finally {
            state.submitted = false;
          }
        }
      }

      return {
        state,
        handlePasswordView,
        handleLogin
      }
    }
  }
</script>

<style>
  .form {
    margin-top: 12em;
    padding: 1em;
  }

  @media screen and (max-width: 648px) {
    .form {
      margin-top: 2em;
    }
  }
</style>
