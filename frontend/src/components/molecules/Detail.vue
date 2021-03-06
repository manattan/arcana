<template>
  <div>
    <v-card flat elevation="0">
      <p class="text-center pt-7 font-weight-bold">
        {{ item.item }}
      </p>
      <h1 v-if="item.percentage > 19" class="text-center mt-5 font-weight-bold">
        {{ Math.round(item.percentage) }}%
      </h1>
      <div v-else>
        <h1 class="text-center mt-5 font-weight-bold danger">
          {{ Math.round(item.percentage) }}%
          <p>残量が少なくなっています。</p>
        </h1>
        <a class="buy" :href="item.url" target="_blank">購入する</a>
      </div>
      <p v-if="displayExp" class="text-center mt-3 font-weight-light">
        消費期限 {{ expirationDate }}
      </p>
      <p
        v-if="!canDelete"
        class="caption text-right mt-10 mr-3 font-weight-light"
      >
        デモ用のデバイスは削除できません。
      </p>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="secondary"
          @click="onClickDelete"
          small
          icon
          :disabled="!canDelete"
          ><v-icon dark> mdi-delete </v-icon></v-btn
        >
        <v-btn color="secondary" text @click="change">変更</v-btn>
        <v-btn color="secondary" text @click="close">閉じる</v-btn>
      </v-card-actions>
    </v-card>
    <v-row justify="center">
      <v-dialog v-model="isOpenChange" max-width="900" hide-overlay>
        <AddDialog
          @close-add-modal="closeChangeModal"
          :deviceId="item.id"
          :name="item.item"
          title="デバイスを変更"
        />
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { deleteDevice } from '../../toServer/v2/index';
import AddDialog from './AddDialog';
import dayjs from 'dayjs';
import { devicesStore } from '../../store/devices';

export default {
  name: 'Detail',

  components: {
    AddDialog,
  },

  props: {
    item: {
      required: true,
      type: Object,
    },
  },

  computed: {
    expirationDate() {
      return dayjs(this.item?.expiration_date).format('YYYY - MM - DD');
    },
    canDelete() {
      return !devicesStore.state.adminIds.includes(this.item?.id);
    },
    displayExp() {
      return !!this.item?.expiration_date;
    },
  },

  data() {
    return {
      isOpenChange: false,
    };
  },

  methods: {
    close() {
      this.$emit('close-detail-modal');
    },

    change() {
      this.$emit('close-detail-modal');
      console.log(this.item)
      this.isOpenChange = true;
    },

    closeChangeModal() {
      this.isOpenChange = false;
    },

    async onClickDelete() {
      try {
        await deleteDevice(this.item.id);
        this.close();
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>

<style scoped>
.danger {
  color: rgb(187, 33, 33) !important;
}

.danger > p {
  font-size: 50%;
}

.buy {
  cursor: pointer;
  user-select: none;
  text-decoration: none;
}
.dialog {
  z-index: 100000;
  border: 1px solid #111;
  border-radius: 10px;
}

.v-card {
  color: #777777;
  font-family: 'Exo', sans-serif;
}

.v-dialog {
  -webkit-box-shadow: 0 0 0;
  box-shadow: 0 0 0;
  border-radius: 10px;
  border: 1px solid #c3c3c3;
}
</style>
