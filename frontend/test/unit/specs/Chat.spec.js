import chat from '../../../src/components/Chat.vue'
import {getPropsVm, getRenderedVm} from './utils.js'
var assert = require('assert')

describe('chat default WIDTH', function () {
    let vm
    it('WIDTH default 600', () => {
        vm = getPropsVm(chat, {
            WIDTH: {
                type: Number,
                default: 600
            }
        })
        assert.equal(600, vm.WIDTH.default)
    })
    it('HEIGHT default 600', () => {
        vm = getPropsVm(chat, {
            HEIGHT: {
                type: Number,
                default: 400
            }
        })
        assert.equal(400, vm.HEIGHT.default)
    })
    it('set width', () => {
        vm = getPropsVm(chat, {
            HEIGHT: 500, WIDTH: 400, BORDER: 1
        })
        assert.equal(500, vm.HEIGHT)
        assert.equal(400, vm.WIDTH)
        assert.equal(1, vm.BORDER)
    })
})