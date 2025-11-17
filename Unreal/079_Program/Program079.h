// Audio Component
// Program 079

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program079.generated.h"

UCLASS()
class AProgram079 : public AActor
{
    GENERATED_BODY()

public:
    AProgram079();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
