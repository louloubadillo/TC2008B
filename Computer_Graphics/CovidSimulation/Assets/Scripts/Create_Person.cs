using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Create_Person : MonoBehaviour
{
    public GameObject PersonPrefab; 
    int numberOfPrefabs = 20; 

    private GameObject newPrefab;


    // Start is called before the first frame update
    void Start()
    {
        for(int i = 0; i < numberOfPrefabs; i++)
        {
            newPrefab = Instantiate(PersonPrefab, new Vector3(Random.Range(-30, 30), 2, Random.Range(-30, 30)), Quaternion.Euler(0,Random.Range(0, 360),0));
            if(i>15){
                newPrefab.tag = "Player";
                newPrefab.GetComponent<Renderer>().material.color = Color.green;
            }
        }


    }

    // Update is called once per frame
    void Update()
    {

    }
}
