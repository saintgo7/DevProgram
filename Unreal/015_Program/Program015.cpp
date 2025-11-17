// Mesh Collision

#include "Program015.h"

AProgram015::AProgram015()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram015::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Mesh Collision ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating mesh collision."));

    // Implement the program logic here...
}

void AProgram015::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
