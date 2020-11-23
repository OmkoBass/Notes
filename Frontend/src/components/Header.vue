<template>
  <header>
    <nav>
      <ul class="p-d-none p-d-md-flex">
        <li>
          <h2
              :class="state.selected === 0 ? 'selected' : null"
              @click="handlePushToCreateNote"
          >
            Create Note
          </h2>
        </li>
        <li>
          <h2
              :class="state.selected === 1 ? 'selected' : null"
              @click="handlePushToAllNotes"
          >
            All Notes
          </h2>
        </li>
        <li>
          <h2
              @click="handleLogout"
          >
            Log out
          </h2>
        </li>
      </ul>

      <div class="p-d-flex p-jc-end">
        <Button
            type="button"
            icon="pi pi-bars"
            class="p-button-rounded p-d-md-none"
            @click="state.mobile = true"
        />
      </div>
    </nav>
  </header>
  <Sidebar v-model:visible="state.mobile" position="right">
    <h2> Links </h2>
    <Menu
        class="p-mt-4"
        style="width: 100%"
        :model="state.menuItems"
    />
  </Sidebar>
</template>

<script>
  import { reactive, watch } from 'vue';
  import router from "@/router";
  import { useRoute } from 'vue-router';

  import Button from 'primevue/button';
  import Sidebar from 'primevue/sidebar';
  import Menu from 'primevue/menu';

  export default {
    name: 'Header',
    components: {
      Button,
      Sidebar,
      Menu
    },
    setup() {
      const route = useRoute();

      const state = reactive({
        selected: null,
        mobile: false,

        menuItems: [
          {
            label: 'Create Note',
            icon: 'pi pi-pencil',
            command: () => {
              router.push({ name: 'CreateNote' });
              state.mobile = false
            }
          },
          {
            label: 'All Notes',
            icon: 'pi pi-folder',
            command: () => {
              router.push({ name: 'AllNotes' });
              state.mobile = false
            }
          }
        ]
      });

      watch(() => route.name, () => {
        if(route.name === 'CreateNote') {
          state.selected = 0;
        } else if (route.name === 'AllNotes') {
          state.selected = 1;
        }
      }, { immediate: true });

      const handlePushToCreateNote = _ => router.push({ name: 'CreateNote' })

      const handlePushToAllNotes = _ => router.push({ name: 'AllNotes' })

      const handleLogout = _ => {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
        router.push({ name: 'Login' });
      }

      return {
        state,
        handlePushToCreateNote,
        handlePushToAllNotes,
        handleLogout
      }
    }
  }
</script>

<style>
header {
  display: flex;
  justify-content: start;
  height: 7vh;
  padding: 1em;
  text-align: center;
  color: white;
  background-color: var(--main-color);
}

nav {
  width: 100%;
}

nav ul{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  list-style-type: none;
}

nav ul li {
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

nav ul li:hover {
  color: lightgray;
}

.selected {
  text-decoration: underline;
}

</style>
