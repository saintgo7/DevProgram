// Sound
// Program 076

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program076.generated.h"

UCLASS()
class AProgram076 : public AActor
{
    GENERATED_BODY()

public:
    AProgram076();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
