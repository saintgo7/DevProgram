// Box Collision
// Program 012

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program012.generated.h"

UCLASS()
class AProgram012 : public AActor
{
    GENERATED_BODY()

public:
    AProgram012();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
