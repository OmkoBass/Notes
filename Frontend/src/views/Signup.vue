<template>
  <div>
    <div class="p-d-flex p-flex-column p-flex-md-row">
      <div class="p-fluid form">

        <h2 class="p-mb-4"> Sign up to Notes </h2>

        <div class="p-field p-grid p-a-center">
          <label for="username" class="p-col-12">Username: </label>
          <div class="p-col-12">
            <InputText id="username" type="text" :class="state.usernameError ? 'p-invalid' : null" class="p-inputtext-lg" v-model="state.username" />
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
            <small id="passwordHelp" :class="state.passwordError ? 'p-invalid' : null">Password must have at least 8 characters.</small>
          </div>
        </div>

        <div class="p-field p-grid p-a-center">
          <label for="confirmPassword" class="p-col-12">Confirm Password: </label>
          <div class="p-col-12">
          <span class="p-input-icon-right">
            <InputText
                id="confirmPassword"
                :type="state.hiddenConfirmPassword ? 'password' : 'text'"
                class="p-inputtext-lg"
                :class="state.confirmPasswordError ? 'p-invalid' : null"
                v-model="state.confirmPassword"
            />
            <i v-if="state.hiddenConfirmPassword" class="pi pi-eye icon" @click="handleConfirmPasswordView" />
            <i v-else class="pi pi-eye-slash icon" @click="handleConfirmPasswordView" />
          </span>
          </div>
        </div>

        <div class="p-field-checkbox p-grid p-md-offset-2 p-ml-2">
          <Checkbox id="agree" name="agree" value="agree" v-model="state.agree" />
          <label for="agree"> I agree to the terms </label>
        </div>

        <div class="p-field-checkbox p-grid p-md-offset-2 p-ml-2">
          <small id="termsHelp">You must agree to the terms.</small>
        </div>

        <div class="p-field p-grid">
          <small id="account">Already an account ? <router-link to="/login"> Click here </router-link> to login! </small>
        </div>

        <div>
          <Button
              :class="state.submitted ? 'p-disabled' : null"
              @click="handleCreateUser"
              label="Signup"
          />
        </div>

        <div class="p-field p-mt-2">
          <ProgressBar v-if="state.submitted" mode="indeterminate"/>
        </div>
      </div>

      <div style="height: 100vh; width: 100%; background-color: #883cae" class="p-d-none p-d-md-inline-flex">
        <div style="color: white; text-align: center; display: block; margin: 16em auto auto auto">
          <h1> NOTES </h1>
          <h2 class="p-mt-2"> Sign up to the best notes app on the net!</h2>
          <h3 class="p-mt-2"> Add notes and edit notes to organize yourself better </h3>
        </div>
      </div>
    </div>
    </div>
  <Toast />

</template>

<script>
  import axios from 'axios';
  import { reactive, computed } from 'vue';

  import Button from 'primevue/button';
  import InputText from 'primevue/inputtext';
  import Checkbox from 'primevue/checkbox';
  import ProgressBar from 'primevue/progressbar';
  import Toast from 'primevue/toast';

  import { useToast } from 'primevue/usetoast';

  import { backend } from '@/utils';
  import router from '@/router';

  export default {
    components: {
      Button,
      InputText,
      Checkbox,
      ProgressBar,
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
          // No, return state.username.length < 4 DOES NOT FUCKING WORK
          if(state.username) {
            const text = state.username;

            return text.length < 4;
          }
        }),

        password: null,
        hiddenPassword: true,
        passwordError: computed(() => {
          if(state.password) {
            const text = state.password;

            return text.length < 8;
          }
        }),

        confirmPassword: null,
        hiddenConfirmPassword: true,
        confirmPasswordError: computed(() => state.confirmPassword !== state.password ),

        agree: false,

        submitted: false,
      });

      const handlePasswordView = _ => state.hiddenPassword = !state.hiddenPassword;
      const handleConfirmPasswordView = _ => state.hiddenConfirmPassword = !state.hiddenConfirmPassword;

      async function handleCreateUser() {
        if(!state.passwordError && !state.confirmPasswordError && state.agree[0] === 'agree') {
            state.submitted = true;

            try {
              const response = await axios.post(`${backend}/api/user/register`, {
                username: state.username,
                password: state.password
              });

              if (response.data === 200)
                await router.push({name: 'Login'})

            } catch(err) {
              toast.add({ severity:'error', summary: 'Error!', detail:'Username already exists!', life: 3000 });
            } finally {
              state.submitted = false;
            }
        }
      }

      return {
        state,
        handlePasswordView,
        handleConfirmPasswordView,
        handleCreateUser
      }
    }
  }
</script>

<style scoped>

</style>
