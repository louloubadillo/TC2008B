using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WaypointController : MonoBehaviour
{
    //list of waypoints
    public List<Transform> waypoints = new List<Transform>();
    //target waypoint
    private Transform targetWaypoint;
    //target waypoint index
    private int targetWaypointIndex = 0;
    //min distance to waypoint
    private float minDistance = 0.1f; 
    //speed 
    public float speed = 5.0f;
    public float rotationSpeed = 5.0f;

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
        float rotationStep = rotationSpeed * Time.deltaTime; 

        Quaternion targetRotation = Quaternion.LookRotation(-(targetWaypoint.position - transform.position));
        transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, rotationStep);

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
}
