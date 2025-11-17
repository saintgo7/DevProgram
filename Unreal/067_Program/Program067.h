// Material Instance
// Program 067

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program067.generated.h"

UCLASS()
class AProgram067 : public AActor
{
    GENERATED_BODY()

public:
    AProgram067();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
