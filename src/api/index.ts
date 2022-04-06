import { type } from "os";
import instance from "./axios";
export const loginHandle = (options: any) => {
    return instance({
        url: "/loginHandle",
        method: options.method,
        data: options.data,
    })
}
export default {
    loginHandle
};