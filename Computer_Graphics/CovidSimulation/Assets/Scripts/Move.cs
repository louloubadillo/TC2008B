using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Move : MonoBehaviour
{
    public List<Transform> waypoints = new List<Transform>();
    private Transform targetWaypoint;
    private int targetWaypointIndex = 0;
    
    private float minDistance = 10.0f; 
    public float speed = 5.0f;

    private int lastWaypointIndex; 
    // Start is called before the first frame update
    void Start()
    {
        lastWaypointIndex = waypoints.Count-1; 
        targetWaypoint = waypoints[targetWaypointIndex];
    }

    // Update is called once per frame
    void Update()
    {
        if(Vector3.Distance(transform.position, waypoints[targetWaypointIndex].position) <= minDistance && targetWaypointIndex <= lastWaypointIndex)
        {
            targetWaypointIndex++; 
            if(targetWaypointIndex > lastWaypointIndex)
            {
                targetWaypointIndex = 0; 
            }
            targetWaypoint = waypoints[targetWaypointIndex];
        }
        transform.position = Vector3.MoveTowards(transform.position, targetWaypoint.position, Time.deltaTime * speed);

        
    }

    private void OnCollisionEnter(Collision collision){
        
        if(collision.gameObject.tag == "Player")
        {
           tag = "Player";
           //change color of player
            GetComponent<Renderer>().material.color=Color.green;

        }
    }
}
