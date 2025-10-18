
const crypto = require('crypto');
const products = [
  {
    product: "carel-modbusrtu",
  },
  {
    product: "cu-modbustcp",
  },
  {
    product: "cu-modbustcp_old",
  },
  {
    product: "freedomline",
  },
  {
    product: "locker-modbusrtu",
  },
  {
    product: "locker-modbustcp",
  },
  {
    product: "mds-modbustcp",
  },
  {
    product: "microds-modbustcp",
  },
];
const productReferences = [
  {
    product: "carel-modbusrtu",
  },
  {
    product: "cu-modbustcp",
  },
  {
    product: "cu-modbustcp_old",
  },
  {
    product: "freedomline",
  },
  {
    product: "locker-modbusrtu",
  },
  {
    product: "locker-modbustcp",
  },
  {
    product: "mds-modbustcp",
  },
  {
    product: "microds-modbustcp",
  },
  {
    product: "pro",
  },
];

const newpro = [];
productReferences.forEach((data) => {
  // eslint-disable-next-line array-callback-return
  products.find((e) => {
    if (e.product !== data.product) {
      newpro.push({ product: data.product });
    }
  });
});
// console.log(newpro);

// let filpro = this.allowedRoles=this.allRoles.filter(role=> !this.assignedRoles.some(present=> present.id==role.id))

// const newproducts = [];
// const filteredProducts = () => products.forEach((e, i) => {
//   const uploadedproducts = productReferences.find((element) => element.product === e.product);
//   newproducts.push(filteredProducts);
//     console.log(newproducts)
// });

// const ResultArrayObjOne = productReferences.filter(({ product: product }) => !products.some(({ product: product }) => product === product));

// console.log(ResultArrayObjOne);

// let resultA = productReferences.filter(ele => !products.map(ele => JSON.stringify(ele)).includes(JSON.stringify(ele)));

// a diff b
// let resultB = products.filter(ele => !productReferences.map(ele => JSON.stringify(ele)).includes(JSON.stringify(ele)));

// show merge
// console.log([...resultA, ...resultB]);

// get random numb
function uid() {
  let a = new Uint32Array(3);
  window.crypto.getRandomValues(a);
  return (
    performance.now().toString(36) +
    Array.from(a)
      .map((A) => A.toString(36))
      .join("")
  ).replace(/\./g, "");
}

// value:'bc7c1a33-eaa6-4009-b085-2ee759d7d521'
        //   a63ae209-ec69-4867-af8a-6f4d1efe15c6
const makeid = (length) => {
  var result = "";
  var characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
};
// console.log(makeid(36))

// let uuid = self.crypto.randomUUID();
// console.log(uuid)
const { uuid } = require('uuidv4');
console.log(uuid());