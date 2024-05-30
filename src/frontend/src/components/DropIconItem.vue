<template>
  <BDropdownItem v-bind="bProps">
    <Icon :name="props.name" />
    <slot />
  </BDropdownItem>
</template>

<script setup lang="ts">
import { type BDropdownItemProps } from "bootstrap-vue-next";

interface propsTypes {
  name: string;
}
interface DropIconItemProps extends propsTypes, BDropdownItemProps {}

const props = defineProps<DropIconItemProps>();
const bProps = Object.fromEntries(
  Object.entries(props).filter(([key]) => !Object.keys(props as propsTypes).includes(key))
) as BDropdownItemProps;
</script>
