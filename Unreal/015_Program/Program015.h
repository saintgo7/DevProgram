// Mesh Collision
// Program 015

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program015.generated.h"

UCLASS()
class AProgram015 : public AActor
{
    GENERATED_BODY()

public:
    AProgram015();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
