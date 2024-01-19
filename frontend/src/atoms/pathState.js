import { atom } from 'recoil';
import { recoilPersist } from 'recoil-persist'
const { persistAtom } = recoilPersist()
export const pathState = atom({
  key: "pathState",
  default: "",
  effects_UNSTABLE: [persistAtom],
});