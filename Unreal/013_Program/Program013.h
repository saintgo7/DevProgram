// Sphere Collision
// Program 013

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program013.generated.h"

UCLASS()
class AProgram013 : public AActor
{
    GENERATED_BODY()

public:
    AProgram013();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
