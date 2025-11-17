// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title EIP712
 * @dev Program 087
 */
contract Program087 {
    // Implement the contract logic here...

    event Log(string message);

    function demo() public {
        emit Log("EIP712");
    }
}
