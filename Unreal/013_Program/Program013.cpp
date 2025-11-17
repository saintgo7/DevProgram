// Sphere Collision

#include "Program013.h"

AProgram013::AProgram013()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram013::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Sphere Collision ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating sphere collision."));

    // Implement the program logic here...
}

void AProgram013::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
